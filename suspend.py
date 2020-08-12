from pynput.mouse import Button, Controller as MouseController
import time
import win32api, win32con

mouse = MouseController()


def pynput_api():
    mouse.position = (25, 845)
    mouse.move(1, 1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.move(-1, -1)

    time.sleep(0.6)

    mouse.move(0, -45)
    time.sleep(0.1)
    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(0.6)

    mouse.move(0, -115)
    time.sleep(0.1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)


def win_btn():
    win32api.SetCursorPos((25, 845))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 25, 845, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 25, 845, 0, 0)


def on_off_btn():
    win32api.SetCursorPos((25, 800))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 25, 800, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 25, 800, 0, 0)


def suspend_btn():
    win32api.SetCursorPos((25, 685))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 25, 685, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 25, 685, 0, 0)


def win32_api():
    win_btn()
    time.sleep(0.3)
    on_off_btn()
    time.sleep(0.3)
    suspend_btn()


pynput_api()
