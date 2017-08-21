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

"""
To install Robot Framework Tftp Library execute command:
    python setup.py install
"""
from distutils.core import setup

setup(name='robotframework-tftplibrary',
      version='1.0',
      description='Robot Framework Tftp Library',
      author='Marcin Kowalczyk',
      author_email='mkov80@gmail.com',
      license='LGPLv3',
      url='https://github.com/kowalpy/Robot-Framework-TFTP-Library/',
      py_modules=['TftpLibrary'],
      install_requires=['tftpy'],
      data_files=[('Example RF script', ['tftp_library_example.txt']),
                  ('Keywords documentation', ['TftpLibrary.html']),
                  ('License file', ['LICENSE'])]
      )