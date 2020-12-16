import os
from ftplib import FTP
from Commands import *

startup()

region = input("Enter the number representin your region.\n[1]USA\n[2]EUR\n[3]PAL\n")

os.chdir("C:\Lord-G\WSC\content")
if region == "1":
    login()
    ftp.cwd('/user/title/0005000e/10144d00/content')
    makefolders()
    extractfiles()
    placefiles()
    complete()
elif region == "2":
    login()
    ftp.cwd('/user/title/0005000e/10144e00/content')
    makefolders()
    extractfiles()
    placefiles()
    complete()
elif region == "3":
    ftp.cwd('/user/title/0005000e/1012f100/content')
    makefolders()
    extractfiles()
    placefiles()
    complete()
else:
    error()