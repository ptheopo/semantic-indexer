# semantic-indexer

**🚧 Work in progress..**

Semantic indexer using Exiftool / RDFLib / Python3 / BerkeleyDB from an hotfolder

## Install

- Install dependancies
- Set your hotfolder path in _hotfolderWatcher.py_ or `mkdir /tmp/hotfolder` (default hotfolder) and set your hotfolder synchronization period (in HotfolderWatcher instanciation)
- Start it `python3 hotfolderWatcher.py`, where you want
- Start client, type `python3 domain.py`
- Insert new medias in your hotfolder
- Go to [127.0.0.1:5000](http://127.0.0.1:5000/)

## Current POC requests

- http://127.0.0.1:5000/files : get all your metadatas
- http://127.0.0.1:5000/filename/<System:FileName> : get multiples or one file(s) metadatas
