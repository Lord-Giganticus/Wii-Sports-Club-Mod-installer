import os
from ftplib import FTP
from Commands import *

region = input("Enter the number representin your region.\n[1]USA\n[2]EUR\n[3]PAL\n")

os.chdir("C:\Lord-G\WSC\content")
if region == "1":
    try:
        login()
        ftp.cwd('/user/title/0005000e/10144d00/content')
        makefolders()
        extractfiles()
        placefiles()
        complete()
    except:
        error(9, 15)
elif region == "2":
    try:
        login()
        ftp.cwd('/user/title/0005000e/10144e00/content')
        makefolders()
        extractfiles()
        placefiles()
        complete()
    except:
        error(19, 25)
elif region == "3":
    try:
        ftp.cwd('/user/title/0005000e/1012f100/content')
        makefolders()
        extractfiles()
        placefiles()
        complete()
    except:
        error(29, 34)
else:
    error(5, 0)