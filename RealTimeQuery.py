from Interactions.SpeechToText import STT
from Interactions.TextToSpeech import TTS
import wikipedia as googleScrap
import wikipedia
import pywhatkit
import webbrowser
import datetime
import psutil

#MY FUNCS
from ChatLogSaver import ChatLog

def telltime():
    current_time = datetime.datetime.now()
    hr = int(current_time.hour)
    mnt = int(current_time.minute)
    tag = ""
    
    if hr >= 12:
        bdhr = abs(hr - 12)
    else:
        bdhr = hr
    
    if hr >= 0 and hr < 12:
        tag = "AM"
    elif hr > 12 and hr <= 24:
        tag = "PM" 
        
    answer = f"The current time is {bdhr} {mnt} {tag}"   
    print(answer)
    TTS(answer)
    
    return answer

class BatteryStatus:
    percentage = ""
    plug = ""
    
    def __init__(self):
        self.battery = psutil.sensors_battery()
        self.percentage = self.battery.percent
        self.plug = "Plugged in." if self.battery.power_plugged else "Not plugged in."
    
    def batteryStatus(self):
        if self.battery is None:
            print("No battery is found...")
            
        print(f"Battery is at {self.percentage}% power and {self.plug}")
        return f"Battery is at {self.percentage}% power and {self.plug}"

def searchGoogle(query):
    query = query.lower()
    query = query.replace("google ", "")
    query = query.replace("look for ", "")
    query = query.replace("google search ", "")
    query = query.replace("search ", "")
    query = query.replace("rose ", "")
    TTS("This is what I found on google")
    
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query, 1)
        TTS(result)
        
        ChatLog(query, result)
        
    except:
        TTS("No speakable output available.")
            
# def searchYoutube(query):
#     if "youtube" in query:
#         TTS("This what I found on Youtube.")
#         query = query.replace("youtube ", "")
#         query = query.replace("youtube search ", "")
#         query = query.replace("search ", "")
#         query = query.replace("search youtube ", "")
#         query = query.replace("rose ", "")
        
#         link = f"https://www.youtube.com/results?search_query={query}"
#         webbrowser.open(link)
#         pywhatkit.playonyt(query) 
#         TTS("Done, sir.")
        
#         ChatLog(query, link)
    
#     if "play" in query:
#         query = query.replace("play ", "")
#         query = query.replace("play on youtube ", "")
#         TTS(f"Playing {query} on youtube ")
        
#         link = f"https://www.youtube.com/results?search_query={query}"
#         webbrowser.open(link)
#         pywhatkit.playonyt(query)
        
#         ChatLog(query, link)
        
        
def searchWikipedia(query):
    TTS("Searching from wikipedia")
    query = query.lower()
    query = query.replace("wikipedia ", "")
    query = query.replace("wikipedia search ", "")
    query = query.replace("search wikipedia ", "")
    query = query.replace("search ", "")
    query = query.replace("rose ", "")
    
    results = wikipedia.summary(query, sentences=2)
    TTS("According to wikipedia.")
    print(results)
    TTS(results)
    
    ChatLog(query, results)
        
def searchFacebook(query):
    TTS("Searching on facebook")
    query = query.lower()
    query = query.replace("search ", "")
    query = query.replace("search on facebook ", "")
    query = query.replace("facebook search ", "")
    query = query.replace("facebook ", "")
    query = query.replace("look for ", "")
    query = query.replace(" ", ".")
    
    fblink = f"https://www.facebook.com/{query}"
    webbrowser.open(fblink)
    TTS("Here's what I found on facebook")
    
    ChatLog(query, fblink)

def searchPerson(query):
    if any(word in query for word in ["who ", "tell me who ", "tell me about ", "who is ", "look for the person ", "person named "]):
        query = query.replace("who is ", "")
        query = query.replace("tell me ", "")
        query = query.replace("tell me about ", "")
        query = query.replace("tell me who is ", "")
        query = query.replace("look for the person named ", "")
    
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query, 1)
        TTS(f"Here's what I found, sir.")
        TTS(result)
        
        ChatLog(query, result)
        
    except:
        TTS("No speakable output available.")
        
    
def RealTimeSearchExecuter(search_query):
    print("Searching...")
    
    google_query = [
        "google",
        "search for",
        "look for"
    ]
    
    peroson_query = [
        "who ", 
        "tell me who ", 
        "tell me about ", 
        "who is ", 
        "look for the person ", 
        "person named "
    ]
    
    if any(q in search_query for q in google_query):
        print("Google query...")
        searchGoogle(search_query)
        
    elif any(q in search_query for q in peroson_query):
        print("Searching a person...")
        searchPerson(search_query)
        
    elif "wikipedia" in search_query:
        print("Wikipedia query...")
        searchWikipedia(search_query)
        
    elif "facebook" in search_query:
        print("Facebook query...")
        searchFacebook(search_query)
        
    else:
        print("No matching search handler found.")
        
    return

if __name__ == "__main__":
    askingtime = [
        "tell me the time",
        "tell the time",
        "what time",
        "what time is it",
        "what time right now"
    ]
    
    realTime = [
        "search on web",
        "web search",
        "search on internet",
        "search for",
        "search",
        "google search",
        "google",
        "youtube",
        "youtube search",
        "search on youtube",
        "search on wikipedia",
        "check on wikipedia",
        "wikipedia",
        "wikipedia search",
        "facebook search",
        "search on facebook",
        "look for",
        "play",
        "play on youtube",
        "who",
        "who is",
        "tell me who is",
        "tell me about"
    ]

    while True: 
        query = STT()
        query = query.lower()
        print(">>> ", query) 
        # search_executer(query) 
        
        if query in askingtime:
            telltime() 
            
        elif any(q in query for q in realTime):
            RealTimeSearchExecuter(query)
            
        else:
            print("No matching query...")
 