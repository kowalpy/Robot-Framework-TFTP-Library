# Robot Framework TFTP Library

This library provides functionality of TFTP client.
[Trivial File Transfer Protocol](https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol)
isn't a complex protocol so the library contains only small amount of keywords. TFTP communication provided by [tftpy](http://tftpy.sourceforge.net/) .

## License

LGPL 3.0

## Keyword documentation

[TftpLibrary.html](https://kowalpy.github.io/Robot-Framework-TFTP-Library/TftpLibrary.html)

Version 1.0 released on 21st of August 2017 

## Installation
- run command: pip install robotframework-tftplibrary

OR

- download, unzip and run command: python setup.py install

## Usage
	
The simplest example (connect, download file, upload file):

```
 | ftp connect | 192.168.1.10             | mylogin | mypassword |
 | cwd         | /home/myname/tmp/testdir |         |            |
 | pwd         |                          |         |            |
 | ftp close   |                          |         |            |
```
