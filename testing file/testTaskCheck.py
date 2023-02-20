
import psutil
 
# Initialzing the wmi constructor
f = psutil.
 
# Printing the header for the later columns
print("pid   Process name")
 
process = f.Win32_Process('Taskmgr.exe')
# Iterating through all the running processes
if "Taskmgr.exe" in process:
    print('yes')