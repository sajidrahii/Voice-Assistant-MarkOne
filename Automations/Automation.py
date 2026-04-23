import AppOpener
from Interactions.SpeechToText import STT
from Interactions.TextToSpeech import TTS
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def clean_query(query, commands):
    for cmd in commands:
        query = query.replace(cmd, "")
        
    return query.strip()

def AppControl(query):
    query = query.lower()
    
    open_cmds = ["start", "open", "turn on", "on"]
    close_cmds = ["close", "shut", "turn off", "off"]
    
    if any(cmd in query for cmd in open_cmds):
        query = clean_query(query, open_cmds)
        
        try:
            print(f"Opening {query}")
            TTS(f"Opening {query}")
            AppOpener.open(query, match_closest=True, output=True, throw_error=True)
            return True
        
        except:
            if query:
                print(f"Searching for {query} on the browser. Do you want it on a new tab?")
                TTS(f"Searching for {query} on the browser. Do you want it on a new tab?")
                ans = STT()
                print(ans)
                
                if ans == "no":
                    webbrowser.open(f"https://www.{query}.com/")
                
                elif ans == "yes":
                    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                    driver.get(f"https://www.{query}.com/")
                return True
            
            else: 
                print(f"Sorry, sir, I could not found anything like {query}")
                TTS(f"Sorry, sir, I could not found anything like {query}")
                return False

    elif any(cmd in query for cmd in close_cmds):
        query = clean_query(query, close_cmds)
        
        try:
            print(f"Closing {query}")
            TTS(f"Closing {query}")
            AppOpener.close(query, match_closest=True)
            return True
        
        except Exception:
            pass
            return False
    
    else:
        print("Please say a valid command like open or close.")
        TTS("Please say a valid command like open or close.")
        return False
        
if __name__ == "__main__":
    while True:
        query = STT()
        print(query)
        AppControl(query)
        