# from Interactions.TextToSpeech import TTS

import webbrowser
import pywhatkit
import pyautogui
import time
import re

youtube_cmd = [
    "play on youtube", "youtube", "youtube play"
    "search youtube", "youtube search", "searh on youtube"
]

def yt_manual_search(txt):
    pyautogui.press("/")
    pyautogui.write(txt)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)

def runYouTube(query):
    # TTS("This what I found on Youtube.")
    
    # Create a regex pattern that matches any of the command phrases
    pattern = r'\b(?:' + '|'.join(map(re.escape, youtube_cmd)) + r')\b'
    # Remove all command phrases from the query
    yt_query = re.sub(pattern, '', query, flags=re.IGNORECASE)
    # Clean up extra whitespace
    yt_query = re.sub(r'\s+', ' ', yt_query).strip()
    print(yt_query)
    
    # link = f"https://www.youtube.com/results?search_query={yt_query}"
    # webbrowser.open(link)
    pywhatkit.playonyt(yt_query)
    
    # TTS("Done, sir.")
        
  
if __name__ == "__main__":
    runYouTube("play on youtube hamnava mere")  