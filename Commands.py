from ftplib import FTP
from os import *

# Made by Lord-Giganticus
version = '1.0.0'
ftp_list = ['/box', '/bsb', '/bwl', '/glf', '/tns']
folder_list = ['box', 'bsb', 'bwl', 'glf', 'tns']
entry = 0
entry_file = 0
length = len(folder_list)
ip = input("Input your wii u's ip.\n")
ftp = FTP(ip)

def debug():
    print('Current version is',version,'use this when reporting bugs.')
    input("")
    exit()
def login():
    ftp.login()
    ftp.cwd('/storage_mlc')
def makefolders():
    mkdir("C:\Lord-G\WSC\Backups\content")
    chdir("C:\Lord-G\WSC\Backups\content")
    while entry <= length:
        mkdir(folder_list[entry])
        entry += 1
def extractfiles():
    chdir("C:\Lord-G\WSC\content")
    while entry <= length:
        ftp.cwd(ftp_list[entry])
        chdir(folder_list[entry])
        file_list = []
        for file in listdir(getcwd()):
            if path.isfile(file) == True:
                file_list.append(file)
        length_file = len(file_list)
        chdir("C:\Lord-G\WSC\Backups\content")
        for entry_file in file_list:
            while entry_file <= length_file:
                localfile = open(file_list[entry_file], 'wb')
                ftp.retrbinary('RETR '+file_list[entry_file], localfile.write)
                entry_file += 1
        entry += 1
def complete():
    input("Complete. Press enter to exit.")
    exit()
def placefiles():
    chdir("C:\Lord-G\WSC\Backups\content")
    length = len(ftp_list)
    while entry <= length:
        ftp.cwd(ftp_list[entry])
        chdir(folder_list[entry])
        for file in listdir(getcwd()):
            if path.isfile(file) == True:
                ftp.storbinary('STOR '+file, open(file, 'rb'))
        entry += 1
def error(x, y):
    if y == 0:
        print("A error occured on line",str(x)+'.')
        input("Press enter to see debug.")
    elif y != 0:
        print("A error has occured in the range of line",str(x),"to line",str(y)+'.')
        input("Press enter to see debug.")
    elif y < 0:
        input("y is lower than 0! y is currently set to",y+".\nThis error is somewhere around line",str(x)+'.\nPlease report this in the issues are of the github repo.\nPress enter to exit.')
        exit()
    debug()