import pyautogui
    
videoControls_key = {
    "play": lambda: pyautogui.press("space"),
    "pause": lambda: pyautogui.press("space"),
    "resume": lambda: pyautogui.press("space"),
    "continue": lambda: pyautogui.press("space"),
    "mute": lambda: pyautogui.press("m"),
    "unmute": lambda: pyautogui.press("m"), 
    "minimize": lambda: pyautogui.press("f"),
    "maximize": lambda: pyautogui.press("f"),
    "seek forward": lambda: pyautogui.press("l"),
    "play forward": lambda: pyautogui.press("l"),
    "seek back": lambda: pyautogui.press("j"),
    "seek backward": lambda: pyautogui.press("j"),
    "forward": lambda: pyautogui.press("l"),
    "backward": lambda: pyautogui.press("j"),
    "volume up": lambda: pyautogui.press("up"),
    "volume down": lambda: pyautogui.press("down"),
    "speed up": lambda: pyautogui.press(">"),
    "slow down": lambda: pyautogui.press("<"),
    "caption on": lambda: pyautogui.press("c"),
    "caption off": lambda: pyautogui.press("c"),
    "subtitle": lambda: pyautogui.press("c")
}
    
def videoControl_executer(query):
    if query in videoControls_key:
        videoControls_key[query]()
        pyautogui.PAUSE = 0.5
    else:
        print("Unable to execute")