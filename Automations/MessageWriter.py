import pyautogui
from Interactions import SpeechToText, TextToSpeech
import AppOpener

from Automations.PressKey import PressKeyFn

def typing():
    TextToSpeech.TTS("Listening to write.")
    text_to_type = SpeechToText.STT()
    
    pyautogui.write(text_to_type)
    pyautogui.press("space")
    pyautogui.PAUSE = 0.5
    
    TextToSpeech.TTS("Done,sir")
    
    return 

def seamless_typing():
    cont = True
    
    while cont:
        
        typing()
        
        TextToSpeech.TTS("should i continue?")
        ans = SpeechToText.STT()
        
        if ans == "keep typing" or ans == "yes" or ans == "keep writing":
            cont = cont
            
        elif ans == "no":
            cont = False
            
        elif ans == "send it" or ans == "press enter":
            PressKeyFn("enter")
            cont = True
        
        else:
            print("Invalid command...")

if __name__ == "__main__":
    seamless_typing()