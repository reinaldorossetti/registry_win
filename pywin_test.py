import win32gui
import win32com.client
import win32con
from time import sleep

shell = win32com.client.Dispatch("WScript.Shell")
hwndMain = win32gui.FindWindow(None, "OpenAM (Login) - Internet Explorer")
print(hwndMain)

# And SetAsForegroundWindow becomes
def SetAsForegroundWindow(hwndMain):
    win32gui.ShowWindow(hwndMain, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(hwndMain)
    sleep(7)

SetAsForegroundWindow(hwndMain)

def send(text):
    shell.SendKeys(text)
    sleep(5)

send('#')
send('{F12}')
send('^2')
send('{TAB}')
send('{TAB}')
send('{TAB}')
send('document')
send('{ENTER}')
send('{ENTER}')



