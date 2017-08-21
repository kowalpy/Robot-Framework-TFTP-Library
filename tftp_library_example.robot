*** Settings ***
Documentation     Example showing how to use robotframework-tftplibrary
Library           TftpLibrary.py    timeout=10

*** Variables ***
${tftp_server_address}    192.168.0.25
${file_name_01}    test_file_01.txt
${local_dir}      c:/Temp

*** Test Cases ***
download_from_tftp_server
    [Documentation]    Example showing how to download files from TFTP server
    Tftp Connect    ${tftp_server_address}
    Tftp Download    ${file_name_01}
    Tftp Download    ${file_name_01}    ${file_name_01}__
    Tftp Download    ${file_name_01}    ${local_dir}
    Tftp Download    ${file_name_01}    ${local_dir}/new_file.txt

upload_to_tftp_server
    [Documentation]    Example showing how to upload files to TFTP server
    Tftp Connect    ${tftp_server_address}
    Tftp Upload    ${file_name_01}
    Tftp Upload    ${file_name_01}    new_file_name_08.txt
    Tftp Upload    ${local_dir}/new_file.txt
    Tftp Upload    ${local_dir}/new_file.txt    new_file_name_108.txt
