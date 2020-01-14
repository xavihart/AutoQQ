import win32gui
import win32con
import win32clipboard as w
import random
import time 

random.seed(5)

def send(s):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, s)
    w.CloseClipboard()
  
#send("aaa")

%imitate the movement of mouse
def main_run(n, m):
    send(m)
    qq = win32gui.FindWindow(None, n)
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

name = "NAME OF WINDOWS"

strlist =  [
  % to do :random words
]

for i in range(1000):
    r = random.randint(0, len(strlist) - 1)
    s = "PROCESS:({:.3f})%%".format(i / 1000 * 100)
    main_run(name, s + ":" + strlist[r])
    main_run(name, strlist[r])
    time.sleep(0.3)

