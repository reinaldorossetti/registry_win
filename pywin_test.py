import win32gui
import win32com.client
import win32con
from time import sleep
from pymouse import PyMouse

shell = win32com.client.Dispatch("WScript.Shell")
hwndMain = win32gui.FindWindow(None, "OpenAM (Login) - Internet Explorer")
print(hwndMain)
mouse = PyMouse()
x, y = 0, 50

# And SetAsForegroundWindow becomes
def SetAsForegroundWindow(hwndMain):
    win32gui.ShowWindow(hwndMain, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(hwndMain)
    sleep(5)

SetAsForegroundWindow(hwndMain)

def send(text):
    shell.SendKeys(text)
    sleep(3)

def move_cursor(x,y):
    # fuction move cursor, below the options.
    mouse.move(x,y)

def click(x,y):
    sleep(3)
    mouse.press(x,y)
    mouse.release(x, y)

def callback(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    print(rect)
    x = rect[0]
    w = rect[2] - x
    print("Window %s:" % win32gui.GetWindowText(hwnd))
    print("\tLocation: (%d, %d)" % (w, y))
    return (w)



send('#')
send('{F12}')
send('^2')
send('{TAB}')
send('{TAB}')
send('{TAB}')

x = callback(hwndMain)
move_cursor(x-10, y)
click(x, y)

send('document')
sleep(5)
send('.mainForm.submit{(}{)}')
send('{ENTER}')
send('{ENTER}')
