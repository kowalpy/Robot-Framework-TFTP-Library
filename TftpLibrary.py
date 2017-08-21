#Robot Framework TFTP Library
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Lesser General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Lesser General Public License for more details.
#
#You should have received a copy of the GNU Lesser General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#to generate libdoc documentation run:
#   python -m robot.libdoc TftpLibrary TftpLibrary.html

import os
from datetime import datetime
import tftpy

class TftpLibrary(object):
    """
This library provides functionality of TFTP client.
[https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol|Trivial File Transfer Protocol]
isn't a complex protocol so the library contains only small amount of keywords.
Very often TFTP communication is used by telecom equipment for purpose of uploading
configuration or getting log files (e.g. Cisco routers).

Version 1.0 released on 21st of August 2017

TFTP communication provided by [http://tftpy.sourceforge.net/|tftpy]

Author: [https://github.com/kowalpy|Marcin Kowalczyk]

Website: https://github.com/kowalpy/Robot-Framework-TFTP-Library

Installation:
- run command: pip install robotframework-tftplibrary

OR
- download, unzip and run command: python setup.py install

The simplest example (connect, download file, upload file):
| Tftp Connect  | ${tftp_server_address} |
| Tftp Download | ${file_name_01}        |
| Tftp Upload   | ${file_name_02}        |
"""

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, timeout=5):
        """
        Library import:
        | Library | TftpLibrary.py |
        Timeout can be configured during import:
        | Library | TftpLibrary.py | 10 |
        """
        self.tftp_client = None
        self.timeout = timeout

    def __check_tftp_client(self):
        if isinstance(self.tftp_client, tftpy.TftpClient):
            return True
        else:
            err_msg_not_init = "Tftp client not initiated. Use Tftp Connect keyword first."
            raise TftpLibraryError(err_msg_not_init)

    def tftp_connect(self, tftp_server_address, port_number=69):
        """
        Initiates tftpy.TftpClient object providing server address and port number.
        Unlike FTP, TFTP does not keep established connection to a server.
        However calling [#Tftp Connect|Tftp Connect ] keyword before other operations
        is a must. To initiate connection to another TFTP server during test just
        call this keyword once again providing valid IP address and port number.

        Parameters:
            - tftp_server_address - TFTP server IP address
            - port_number(optional) - TFTP server port number, by default 69

        Example:
        | Tftp Connect | ${tftp_server_address} |
        """
        try:
            self.tftp_client = tftpy.TftpClient(tftp_server_address, port_number)
        except Exception as e:
            raise TftpLibraryError(e)

    def tftp_upload(self, local_file_path, remote_file_name=None):
        """
        Sends file from local drive to TFTP server. Before calling this keyword,
        [#Tftp Connect|Tftp Connect ] must be called.

        Parameters:
        - local_file_path - file name or path to a file on a local drive
        - remote_file_name (optional) - a name under which file should be saved
        If remote_file_name agument is not given, local name would be used

        Examples:
        | tftp upload | test_file_01.txt |  |
        | tftp upload | test_file_01.txt | new_file_name_08.txt |
        | tftp upload | c:/Temp/new_file.txt |  |
        | tftp upload | c:/Temp/new_file.txt | new_file_name_108.txt |
        """
        if self.__check_tftp_client():
            remote_file = ""
            local_file_path = os.path.normpath(local_file_path)
            if not os.path.isfile(local_file_path):
                raise TftpLibraryError("%s is no a valid file path" % local_file_path)
            else:
                if remote_file_name == None:
                    file_tuple = os.path.split(local_file_path)
                    if len(file_tuple)==2:
                        remote_file = file_tuple[1]
                    else:
                        timestamp = datetime.now().strftime("%H%M%S%f")
                        remote_file = timestamp
                else:
                    remote_file = remote_file_name
            try:
                local_file_path = str(local_file_path)
                remote_file = str(remote_file)
                self.tftp_client.upload(remote_file, local_file_path)
            except Exception as e:
                raise TftpLibraryError(e)

    def tftp_download(self, remote_file_name, local_file_path=None):
        """
        Downloads file from TFTP server. Before calling this keyword,
        [#Tftp Connect|Tftp Connect ] must be called.


        Parameters:
        - remote_file_name - file name on TFTP server
        - local_file_path (optional) - local file name or path where remote file
         should be saved
        If local_file_path is not given, file is saved in current local directory
        (by default folder containing robot framework project file) with the same
        name as source file

        Examples:
        | tftp download | test_file_01.txt |  |
        | tftp download | test_file_01.txt | test_file_01.txt__ |
        | tftp download | test_file_01.txt | c:/Temp |
        | tftp download | test_file_01.txt | c:/Temp/new_file.txt |
        """
        if self.__check_tftp_client():
            local_path = ""
            if local_file_path == None:
                local_path = remote_file_name
            else:
                local_path = os.path.normpath(local_file_path)
                if os.path.isdir(local_path):
                    local_path = os.path.join(local_path, remote_file_name)
            try:
                remote_file_name = str(remote_file_name)
                local_path = str(local_path)
                self.tftp_client.download(remote_file_name, local_path)
            except Exception as e:
                raise TftpLibraryError(e)

class TftpLibraryError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

def main():
    print "Robot Framework TFTP library. Not intended to run as standalone process. "
    print "Webpage: https://github.com/kowalpy/Robot-Framework-TFTP-Library"

if __name__ == '__main__':
    main()