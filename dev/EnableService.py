import winreg as wr


HKCU = wr.HKEY_CURRENT_USER
CMD_REG = r'SOFTWARE\\Policies\\Microsoft\\Windows\\System'
TASKMGR_REG = r"SOFTWARE\\Microsoft\Windows\\CurrentVersion\\Policies\System"

def EnableCMD(HKCU, CMD_REG):
    key = wr.CreateKey(HKCU, CMD_REG)
    wr.DeleteValue(key, r'DisableCMD')


def EnableTaskMgr(HKCU, TASKMGR_REG):
    key = wr.CreateKey(HKCU, TASKMGR_REG)
    wr.DeleteValue(key, r'DisableTaskMgr')
    
    
EnableCMD(HKCU, CMD_REG)
EnableTaskMgr(HKCU, TASKMGR_REG)
