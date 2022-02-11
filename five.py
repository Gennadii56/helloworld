import sys
import subprocess
if sys.platform == 'win32': 
    subprocess.call ([ 'C:/Program Files/Notepad++/notepad++.exe'])
elif sys.platform == 'linux':
    subprocess . call ([ 'gimp'])
