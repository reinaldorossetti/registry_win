import win32gui

toplist = []
winlist = []

def enum_callback(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

win32gui.EnumWindows(enum_callback, toplist)
firefox = [(hwnd, title) for hwnd, title in winlist if 'firefox' in title.lower()]

# just grab the first window that matches
firefox = firefox[0]

# use the window handle to set focus
win32gui.SetForegroundWindow(firefox[0])

# To minimize the window, the following line:
import win32con
win32gui.ShowWindow(firefox[0], win32con.SW_MINIMIZE)
