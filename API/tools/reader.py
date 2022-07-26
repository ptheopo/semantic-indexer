import sys
from importlib.resources import Resource

from rdflib import *
from rdflib import URIRef

graph = ConjunctiveGraph(store="BerkeleyDB")

# first time create the store:
graph.open('/tmp/store', create=False)

req = """
PREFIX System: <http://ns.exiftool.org/File/System/1.0/>
PREFIX File: <http://ns.exiftool.org/File/1.0/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX et: <http://ns.exiftool.org/1.0/>
PREFIX ExifTool: <http://ns.exiftool.org/ExifTool/1.0/>
PREFIX JFIF: <http://ns.exiftool.org/JFIF/JFIF/1.0/>
PREFIX Composite: <http://ns.exiftool.org/Composite/1.0/>
PREFIX GIF: <http://ns.exiftool.org/GIF/GIF/1.0/>
PREFIX ICC_Profile: <http://ns.exiftool.org/ICC_Profile/ICC_Profile/1.0/>
PREFIX PNG: <http://ns.exiftool.org/PNG/PNG/1.0/>
PREFIX Adobe: <http://ns.exiftool.org/APP14/Adobe/1.0/>
PREFIX SVG: <http://ns.exiftool.org/SVG/SVG/1.0/>
PREFIX ExifIFD: <http://ns.exiftool.org/EXIF/ExifIFD/1.0/>
PREFIX ZIP: <http://ns.exiftool.org/ZIP/ZIP/1.0/>
PREFIX IFD0: <http://ns.exiftool.org/EXIF/IFD0/1.0/>
PREFIX ICC-header: <http://ns.exiftool.org/ICC_Profile/ICC-header/1.0/>
PREFIX ICC-view: <http://ns.exiftool.org/ICC_Profile/ICC-view/1.0/>
PREFIX ICC-meas: <http://ns.exiftool.org/ICC_Profile/ICC-meas/1.0/>
PREFIX IPTC: <http://ns.exiftool.org/IPTC/IPTC/1.0/>
PREFIX XMP: <http://ns.exiftool.org/XMP/XMP/1.0/>

CONSTRUCT {
    
    ?subj ?pred ?obj
    
} WHERE {
    
    ?subj ?pred ?obj .

    ?subj System:FileName "ed.jpeg" .

}
"""

result = graph.query(req)

result.graph.namespace_manager.bind('System', "http://ns.exiftool.org/File/System/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('File', "http://ns.exiftool.org/File/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('rdf', "http://www.w3.org/1999/02/22-rdf-syntax-ns#", override=True, replace=True)
result.graph.namespace_manager.bind('et', "http://ns.exiftool.org/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('ExifTool', "http://ns.exiftool.org/ExifTool/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('JFIF', "http://ns.exiftool.org/JFIF/JFIF/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('Composite', "http://ns.exiftool.org/Composite/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('GIF', "http://ns.exiftool.org/GIF/GIF/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('ICC_Profile', "http://ns.exiftool.org/ICC_Profile/ICC_Profile/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('PNG', "http://ns.exiftool.org/PNG/PNG/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('Adobe', "http://ns.exiftool.org/APP14/Adobe/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('SVG', "http://ns.exiftool.org/SVG/SVG/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('ExifIFD', "http://ns.exiftool.org/EXIF/ExifIFD/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('ZIP', "http://ns.exiftool.org/ZIP/ZIP/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('IFD0', "http://ns.exiftool.org/EXIF/IFD0/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('ICC-header', "http://ns.exiftool.org/ICC_Profile/ICC-header/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('ICC-view', "http://ns.exiftool.org/ICC_Profile/ICC-view/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('ICC-meas', "http://ns.exiftool.org/ICC_Profile/ICC-meas/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('IPTC', "http://ns.exiftool.org/IPTC/IPTC/1.0/", override=True, replace=True)
result.graph.namespace_manager.bind('XMP', "http://ns.exiftool.org/XMP/XMP/2.0/", override=True, replace=True)

result.serialize("sparql.xml")

graph.close()
