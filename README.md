# Robot Framework TFTP Library

This library provides functionality of TFTP client.
[Trivial File Transfer Protocol](https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol)
isn't a complex protocol so the library contains only small amount of keywords. TFTP communication provided by [tftpy](http://tftpy.sourceforge.net/) .

## License

LGPL 3.0

## Keyword documentation

[TftpLibrary.html](https://kowalpy.github.io/Robot-Framework-TFTP-Library/TftpLibrary.html)

## Version history

Version 1.0 released on 21st of August 2017 

Version 1.1 released on 25th of December 2017  

What's new in release 1.1:
- python 3 support
- setup bugfix by Jinhyuk.Im

## Installation
- run command: pip install robotframework-tftplibrary

OR

- download, unzip and run command: python setup.py install

## Usage
	
The simplest example (connect, download file, upload file):

```
	| Tftp Connect  | ${tftp_server_address} |
	| Tftp Download | ${file_name_01}        |
	| Tftp Upload   | ${file_name_02}        |
```
