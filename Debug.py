import subprocess
from colorama import Fore
import os

def cmdline():
    subprocess.Popen(['start' , 'cmd.exe'], shell=True)
    
def powerline():
    subprocess.Popen(['start' , 'powershell.exe'], shell=True)
    
def explorer():
    subprocess.Popen(['start' , 'explorer.exe'], shell=True)

def regedit():
    subprocess.Popen(['start' , 'regedit.exe'], shell=True)
    
def notepad():
    subprocess.Popen(['start' , 'notepad.exe'], shell=True)
    
def Services():
    subprocess.Popen(['start' , 'services.msc'], shell=True)
    
def Taskmgr():
    subprocess.Popen({start, 'taskmgr.exe'}, shell=True)
    
def gpedit():
    subprocess.Popen(['start' , 'gpedit.exe'], shell=True)
    
def msconfig():
    subprocess.Popen(['start' , 'msconfig.exe'], shell=True)
    
def TaskSchedule():
    subprocess.Popen(['start' , 'schtasks.msc'], shell=True)
    
print(Fore.LIGHTRED_EX + "Debug Tool By CodeCraft")
print(Fore.LIGHTYELLOW_EX + "Tools:")
print(Fore.LIGHTCYAN_EX + '1: Command Prompt')
print(Fore.LIGHTBLUE_EX + '2: PowerShell')
print(Fore.LIGHTWHITE_EX + '3: Explorer')
print(Fore.LIGHTRED_EX + '4: Registry Editor')
print(Fore.LIGHTBLUE_EX + '5: Services')
print(Fore.LIGHTWHITE_EX + '6: Group Policy Editor')
print(Fore.LIGHTGREEN_EX + '7: Notepad')
print(Fore.LIGHTGREEN_EX + '8: Task Manager')
print(Fore.LIGHTGREEN_EX + '9: Msconfig Editor')
print(Fore.LIGHTRED_EX + '10: Task Scheduler')
ask = input(Fore.LIGHTRED_EX + '(Use The Number Assigned To Each Tool)Which Tool To Use?: ')
if ask == "1":
    cmdline()
    os.system('python Debug_Tool.py')
elif ask == "2":
    powerline()
    os.system('python Debug_Tool.py')
elif ask == "3":
    explorer()
    os.system('python Debug_Tool.py')
elif ask == "4":
    regedit()
    os.system('python Debug_Tool.py')
elif ask == "5":
    Services()
    os.system('python Debug_Tool.py')
elif ask == "6":
    gpedit()
    os.system('python Debug_Tool.py')
elif ask == "7":
    notepad()
    os.system('python Debug_Tool.py')
elif ask == "8":
    Taskmgr()
    os.system('python Debug_Tool.py')
elif ask == "9":
    msconfig()
    os.system('python Debug_Tool.py')
elif ask == "10":
    TaskSchedule()
    os.system('python Debug_Tool.py')
else:
    print('Invalid Option')
    print('Restarting The Tool...')
    os.system('python Debug_Tool.py')
