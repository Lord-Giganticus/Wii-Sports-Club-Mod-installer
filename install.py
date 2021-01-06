import os
from shutil import move
program_location = os.getcwd()

if os.path.isfile("install.py") == False:
    input("The script isn't in the folder your running this script in somehow! Press enter to exit.")
    exit()
if os.path.isdir("C:\Lord-G\Scripts") == False:
    os.mkdir("C:\Lord-G\Scripts")
os.chdir("C:\Lord-G\Scripts")
if os.path.isfile("Commands.py") == False:
    os.system('cmd /c curl https://lord-giganticus.github.io/Wii-Sports-Club-Mod-installer/files/Commands.py -o Commands.py')
from Commands import error
try:
    if os.path.isfile("Wii Sports Club Mod Installer.py") == False:
        os.system('cmd /c curl https://lord-giganticus.github.io/Wii-Sports-Club-Mod-installer/files/Wii%20Sports%20Club%20Mod%20Installer.py -o "Wii Sports Club Mod Installer.py"')
except:
    error(15, 16)
else:
    input("Complete. Press enter to exit the program and open the folder.")
    os.chdir(program_location)
    move_install = input("Do you want to move install.py?\n If so enter 1.\nIf you don't want to just press enter.\n")
    if move_install == "1":
        move("install.py", "C:\Lord-G\Scripts\install.py")
    os.system('cmd /c start C:\Lord-G\Scripts')
    