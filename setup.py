try:
    import pyfiglet
    import subprocess
    import os
    import re
    from colorama import * 
except ImportError:
    os.system("pip3 install pyfiglet", shell=True)


os.system("cls")

ascii_banner = pyfiglet.figlet_format("Welcome to SysInfo")
print(ascii_banner)
init()
print(Fore.YELLOW + " [+] Speakup is a program which gets you detailed information about your system")
print(Style.RESET_ALL)
input("\n[+] Press Enter to start the setup >> ")
os.system("pip install numpy")
os.system("pip install matplotlib")
os.system("pip install psutil")
os.system("pip install wmi")

 

os.system("python SysInfo.py")
