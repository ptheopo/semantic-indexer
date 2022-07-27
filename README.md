# semantic-indexer

**🚧 Work in progress..**

Semantic indexer using Exiftool / RDFLib / Python3 / BerkeleyDB from an hotfolder

## Install

- Install dependancies
- Set your hotfolder path in _hotfolderWatcher.py_ or `mkdir /tmp/hotfolder` (default hotfolder) and set your hotfolder synchronization period (in HotfolderWatcher instanciation)
- Start it `python3 hotfolderWatcher.py`, where you want
- Start client, type `python3 domain.py`
- Insert new medias in your hotfolder
- Go to [127.0.0.1:5000](http://127.0.0.1:5000/) for checking API
- Install web app client in APP, type `cd APP && npm install`
- Run web app, `node app.js`
- Go to [127.0.0.1:8081](http://127.0.0.1:8081/) for viewing web app

*ℹ️ docker-compose part is currently in working*

## Current POC requests

- http://127.0.0.1:5000/files : get all your metadatas
- http://127.0.0.1:5000/filename/<System:FileName> : get multiples or one file(s) metadatas

## Metadatas

Semantic Indexer use ExifTool, in particular `exiftool -X <filename>` for getting RDF resources

> ExifTool is a platform-independent Perl library plus a command-line application for reading, writing and editing meta information in a wide variety of files. ExifTool supports many different metadata formats including EXIF, GPS, IPTC, XMP, JFIF, GeoTIFF, ICC Profile, Photoshop IRB, FlashPix, AFCP and ID3, Lyrics3, as well as the maker notes of many digital cameras by Canon, Casio, DJI, FLIR, FujiFilm, GE, GoPro, HP, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Motorola, Nikon, Nintendo, Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Phase One, Reconyx, Ricoh, Samsung, Sanyo, Sigma/Foveon and Sony. - https://exiftool.org

## Examples

- http://127.0.0.1:5000/files

```xml
<rdf:RDF xmlns:Composite="http://ns.exiftool.org/Composite/1.0/" xmlns:ExifTool="http://ns.exiftool.org/ExifTool/1.0/" xmlns:File="http://ns.exiftool.org/File/1.0/" xmlns:JFIF="http://ns.exiftool.org/JFIF/JFIF/1.0/" xmlns:PNG="http://ns.exiftool.org/PNG/PNG/1.0/" xmlns:System="http://ns.exiftool.org/File/System/1.0/" xmlns:ZIP="http://ns.exiftool.org/ZIP/ZIP/1.0/" xmlns:et="http://ns.exiftool.org/1.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="/tmp/hotfolder/Backgrounds/as.jpg">
    <System:FileSize>183 KiB</System:FileSize>
    <System:FileModifyDate>2022:07:14 14:06:31+02:00</System:FileModifyDate>
    <System:FileAccessDate>2022:07:14 14:06:31+02:00</System:FileAccessDate>
    <System:FileInodeChangeDate>2022:07:14 14:06:31+02:00</System:FileInodeChangeDate>
    <System:FilePermissions>-rw-rw-r--</System:FilePermissions>
    <File:FileType>JPEG</File:FileType>
    <File:FileTypeExtension>jpg</File:FileTypeExtension>
    <File:MIMEType>image/jpeg</File:MIMEType>
    <File:Comment>CREATOR: gd-jpeg v1.0 (using IJG JPEG v62), quality = 75 </File:Comment>
    <File:ImageWidth>1500</File:ImageWidth>
    <File:ImageHeight>1000</File:ImageHeight>
    <et:toolkit>Image::ExifTool 12.40</et:toolkit>
    <File:EncodingProcess>Baseline DCT, Huffman coding</File:EncodingProcess>
    <File:BitsPerSample>8</File:BitsPerSample>
    <File:ColorComponents>3</File:ColorComponents>
    <File:YCbCrSubSampling>YCbCr4:2:0 (2 2)</File:YCbCrSubSampling>
    <JFIF:JFIFVersion>1.01</JFIF:JFIFVersion>
    <JFIF:ResolutionUnit>None</JFIF:ResolutionUnit>
    <JFIF:XResolution>1</JFIF:XResolution>
    <JFIF:YResolution>1</JFIF:YResolution>
    <Composite:ImageSize>1500x1000</Composite:ImageSize>
    <Composite:Megapixels>1.5</Composite:Megapixels>
    <ExifTool:ExifToolVersion>12.40</ExifTool:ExifToolVersion>
    <System:FileName>as.jpg</System:FileName>
    <System:Directory>/tmp/hotfolder/Backgrounds</System:Directory>
  </rdf:Description>
  <rdf:Description rdf:about="/tmp/hotfolder/Captures d’écran/Capture d’écran du 2022-07-01 16-23-34.png">
    <System:FileSize>485 KiB</System:FileSize>
    <System:FileModifyDate>2022:07:14 14:06:32+02:00</System:FileModifyDate>
    <System:FileAccessDate>2022:07:14 14:06:32+02:00</System:FileAccessDate>
    <System:FileInodeChangeDate>2022:07:14 14:06:32+02:00</System:FileInodeChangeDate>
    <System:FilePermissions>-rw-rw-r--</System:FilePermissions>
    <File:FileType>PNG</File:FileType>
    <File:FileTypeExtension>png</File:FileTypeExtension>
    <File:MIMEType>image/png</File:MIMEType>
    <et:toolkit>Image::ExifTool 12.40</et:toolkit>
    <Composite:ImageSize>1366x768</Composite:ImageSize>
    <Composite:Megapixels>1.0</Composite:Megapixels>
    <ExifTool:ExifToolVersion>12.40</ExifTool:ExifToolVersion>
    <PNG:ImageWidth>1366</PNG:ImageWidth>
    <PNG:ImageHeight>768</PNG:ImageHeight>
    <PNG:BitDepth>8</PNG:BitDepth>
    <PNG:ColorType>RGB with Alpha</PNG:ColorType>
    <System:FileName>Capture d’écran du 2022-07-01 16-23-34.png</System:FileName>
    <PNG:Compression>Deflate/Inflate</PNG:Compression>
    <PNG:Filter>Adaptive</PNG:Filter>
    <PNG:Interlace>Noninterlaced</PNG:Interlace>
    <PNG:SignificantBits>8 8 8 8</PNG:SignificantBits>
    <PNG:Software>gnome-screenshot</PNG:Software>
    <PNG:CreationTime>ven. 01 juil. 2022 16:23:34</PNG:CreationTime>
    <System:Directory>/tmp/hotfolder/Captures d’écran</System:Directory>
  </rdf:Description>
  <rdf:Description rdf:about="/tmp/hotfolder/Captures d’écran/Capture d’écran du 2022-07-04 23-01-11.png">
    <System:FileSize>320 KiB</System:FileSize>
    <System:FileModifyDate>2022:07:14 14:06:32+02:00</System:FileModifyDate>
    <System:FileAccessDate>2022:07:14 14:06:32+02:00</System:FileAccessDate>
    <System:FileInodeChangeDate>2022:07:14 14:06:32+02:00</System:FileInodeChangeDate>
    <System:FilePermissions>-rw-rw-r--</System:FilePermissions>
    <File:FileType>PNG</File:FileType>
    <File:FileTypeExtension>png</File:FileTypeExtension>
    <File:MIMEType>image/png</File:MIMEType>
    <et:toolkit>Image::ExifTool 12.40</et:toolkit>
    <Composite:ImageSize>634x603</Composite:ImageSize>
    <Composite:Megapixels>0.382</Composite:Megapixels>
    <ExifTool:ExifToolVersion>12.40</ExifTool:ExifToolVersion>
    <PNG:ImageWidth>634</PNG:ImageWidth>
    <PNG:ImageHeight>603</PNG:ImageHeight>
    <PNG:BitDepth>8</PNG:BitDepth>
    <PNG:ColorType>RGB with Alpha</PNG:ColorType>
    <System:FileName>Capture d’écran du 2022-07-04 23-01-11.png</System:FileName>
    <PNG:Compression>Deflate/Inflate</PNG:Compression>
    <PNG:Filter>Adaptive</PNG:Filter>
    <PNG:Interlace>Noninterlaced</PNG:Interlace>
    <PNG:SignificantBits>8 8 8 8</PNG:SignificantBits>
    <PNG:Software>gnome-screenshot</PNG:Software>
    <PNG:CreationTime>lun. 04 juil. 2022 23:01:11</PNG:CreationTime>
    <System:Directory>/tmp/hotfolder/Captures d’écran</System:Directory>
  </rdf:Description>
  <rdf:Description rdf:about="/tmp/hotfolder/Captures d’écran/Capture d’écran du 2022-07-02 16-47-24.png">
    <System:FileSize>673 KiB</System:FileSize>
    <System:FileModifyDate>2022:07:14 14:06:32+02:00</System:FileModifyDate>
    <System:FileAccessDate>2022:07:14 14:06:32+02:00</System:FileAccessDate>
    <System:FileInodeChangeDate>2022:07:14 14:06:32+02:00</System:FileInodeChangeDate>
    <System:FilePermissions>-rw-rw-r--</System:FilePermissions>
    <File:FileType>PNG</File:FileType>
    <File:FileTypeExtension>png</File:FileTypeExtension>
    <File:MIMEType>image/png</File:MIMEType>
    <et:toolkit>Image::ExifTool 12.40</et:toolkit>
    <Composite:ImageSize>1338x650</Composite:ImageSize>
    <Composite:Megapixels>0.870</Composite:Megapixels>
    <ExifTool:ExifToolVersion>12.40</ExifTool:ExifToolVersion>
    <PNG:ImageWidth>1338</PNG:ImageWidth>
    <PNG:ImageHeight>650</PNG:ImageHeight>
    <PNG:BitDepth>8</PNG:BitDepth>
    <PNG:ColorType>RGB with Alpha</PNG:ColorType>
    <System:FileName>Capture d’écran du 2022-07-02 16-47-24.png</System:FileName>
    <PNG:Compression>Deflate/Inflate</PNG:Compression>
    <PNG:Filter>Adaptive</PNG:Filter>
    <PNG:Interlace>Noninterlaced</PNG:Interlace>
    <PNG:SignificantBits>8 8 8 8</PNG:SignificantBits>
    <PNG:Software>gnome-screenshot</PNG:Software>
    <PNG:CreationTime>sam. 02 juil. 2022 16:47:24</PNG:CreationTime>
    <System:Directory>/tmp/hotfolder/Captures d’écran</System:Directory>
  </rdf:Description>
  <rdf:Description rdf:about="/tmp/hotfolder/Backgrounds/Non confirmé 757721.crdownload">
    <System:FileSize>383 MiB</System:FileSize>
    <System:FileModifyDate>2022:07:14 14:06:32+02:00</System:FileModifyDate>
    <System:FileAccessDate>2022:07:14 14:06:31+02:00</System:FileAccessDate>
    <System:FileInodeChangeDate>2022:07:14 14:06:32+02:00</System:FileInodeChangeDate>
    <System:FilePermissions>-rw-rw-r--</System:FilePermissions>
    <File:FileType>GZIP</File:FileType>
    <File:FileTypeExtension>gz</File:FileTypeExtension>
    <File:MIMEType>application/x-gzip</File:MIMEType>
    <et:toolkit>Image::ExifTool 12.40</et:toolkit>
    <ZIP:Compression>Deflated</ZIP:Compression>
    <ZIP:Flags>(none)</ZIP:Flags>
    <ExifTool:ExifToolVersion>12.40</ExifTool:ExifToolVersion>
    <ZIP:ModifyDate>0000:00:00 00:00:00</ZIP:ModifyDate>
    <ZIP:ExtraFlags>(none)</ZIP:ExtraFlags>
    <ZIP:OperatingSystem>FAT filesystem (MS-DOS, OS/2, NT/Win32)</ZIP:OperatingSystem>
    <System:FileName>Non confirmé 757721.crdownload</System:FileName>
    <System:Directory>/tmp/hotfolder/Backgrounds</System:Directory>
  </rdf:Description>
</rdf:RDF>
```

- http://127.0.0.1:5000/filename/<System:FileName>

```xml
<rdf:RDF xmlns:Composite="http://ns.exiftool.org/Composite/1.0/" xmlns:ExifTool="http://ns.exiftool.org/ExifTool/1.0/" xmlns:File="http://ns.exiftool.org/File/1.0/" xmlns:PNG="http://ns.exiftool.org/PNG/PNG/1.0/" xmlns:System="http://ns.exiftool.org/File/System/1.0/" xmlns:et="http://ns.exiftool.org/1.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="/tmp/hotfolder/Captures d’écran/Capture d’écran du 2022-07-01 16-23-34.png">
    <System:FileSize>485 KiB</System:FileSize>
    <System:FileModifyDate>2022:07:14 14:06:32+02:00</System:FileModifyDate>
    <System:FileAccessDate>2022:07:14 14:06:32+02:00</System:FileAccessDate>
    <System:FileInodeChangeDate>2022:07:14 14:06:32+02:00</System:FileInodeChangeDate>
    <System:FilePermissions>-rw-rw-r--</System:FilePermissions>
    <File:FileType>PNG</File:FileType>
    <File:FileTypeExtension>png</File:FileTypeExtension>
    <File:MIMEType>image/png</File:MIMEType>
    <et:toolkit>Image::ExifTool 12.40</et:toolkit>
    <Composite:ImageSize>1366x768</Composite:ImageSize>
    <Composite:Megapixels>1.0</Composite:Megapixels>
    <ExifTool:ExifToolVersion>12.40</ExifTool:ExifToolVersion>
    <PNG:ImageWidth>1366</PNG:ImageWidth>
    <PNG:ImageHeight>768</PNG:ImageHeight>
    <PNG:BitDepth>8</PNG:BitDepth>
    <PNG:ColorType>RGB with Alpha</PNG:ColorType>
    <System:FileName>Capture d’écran du 2022-07-01 16-23-34.png</System:FileName>
    <PNG:Compression>Deflate/Inflate</PNG:Compression>
    <PNG:Filter>Adaptive</PNG:Filter>
    <PNG:Interlace>Noninterlaced</PNG:Interlace>
    <PNG:SignificantBits>8 8 8 8</PNG:SignificantBits>
    <PNG:Software>gnome-screenshot</PNG:Software>
    <PNG:CreationTime>ven. 01 juil. 2022 16:23:34</PNG:CreationTime>
    <System:Directory>/tmp/hotfolder/Captures d’écran</System:Directory>
  </rdf:Description>
</rdf:RDF>
```
