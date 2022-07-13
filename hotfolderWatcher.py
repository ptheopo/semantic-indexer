import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rdflib import Graph
from subprocess import Popen, PIPE

g_paths = []
g_items = 0

#########
# STORE #
#########

class RDFStore:

    def __init__(self, dbPath):
        self.graph = Graph(store='BerkeleyDB')
        self.dbPath = dbPath
        self.graph.open(self.dbPath, create=True)

    def close():
        self.graph.close();

#############
# HOTFOLDER #
#############

class HotfolderWatcher:

    def __init__(self, directory, period):
        self.observer = Observer()
        self.rdfStore = RDFStore("/tmp/store")
        self.directory = directory
        self.period = period

    def sync(self, paths, items):
        
        createdPaths = []
        print("[SYNC] Exiftool get RDF output from :")
        for path in paths:
            print("\t| " + path[1])
            if path[0] == 0:
                createdPaths.append(path[1])
        process = Popen(['exiftool', '-X'] + createdPaths, stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()
        print("[SYNC] Synchronize " + self.directory +  " hotfolder")
        self.rdfStore.graph.parse(data=output.decode("utf-8"), format="xml")

    def run(self):

        global g_paths
        global g_items

        event_handler = HotfolderHandler()
        self.observer.schedule(event_handler, self.directory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(self.period)
                items = g_items
                if items > 0 and g_paths != []:
                    self.sync(g_paths, items)
                    g_paths = g_paths[items:]
                    g_items -= items

        except Exception as e:
            self.observer.stop()
            print("Observer Stopped")
            print(e)

        self.observer.join()

class HotfolderHandler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        global g_paths
        global g_items

        # Inside _paths_ property, first index :
        # 0 => New created file
        # 1 => New modified file
        # 2 => New deleted file
        # second index :
        # This is the absolute path

        if event.is_directory:
            return None
        elif event.event_type == 'created':
            # Event is created, you can process it now
            g_items += 1
            g_paths.append((0, event.src_path))
            print("Watchdog received created event - % s." % event.src_path)
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event - % s." % event.src_path)

########
# MAIN #
########

watch = HotfolderWatcher("/tmp/hotfolder", 5)
watch.run()
