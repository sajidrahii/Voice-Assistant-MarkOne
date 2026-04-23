import os
import pyautogui

file_path = r"Frontend\Mark.gif"

def initial_frontend():
    os.startfile(filepath=file_path)
    pyautogui.countdown(3)
    pyautogui.press("f11")
    
def kill_frontend():
    os.abort()
    exit()
    
    