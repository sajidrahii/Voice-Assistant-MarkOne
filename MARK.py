#Updates
#THE realtime didnt worked

import datetime
from colorama import Fore

#MY FUNCS
from Interactions.TextToSpeech import TTS
from Interactions.SpeechToText import STT
import RealTimeQuery, Chatbot_v2, ChatLogSaver
from FaceRecognition.facerec_v2 import FaceRecognition_v2


from Automations.YouTube import video_controls
from Automations.Automation import AppControl
from Automations.FileExplorer import fileExplorer
from Automations.Social_Media import SocialMedia_qm 
from Automations.YouTube import youtube
from Automations.MessageWriter import seamless_typing
from Automations.PressKey import PressKeyFn
from Frontend import initial
import input_lists


def GreetMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour <= 12:
        TTS("Good morning. At your service,sir.")
        
    elif hour > 12 and hour <= 18:
        TTS("Good afternoon. At your service,sir.")
        
    else:
        TTS("Good evening. At your service,sir.")
        
def EnableRose():
    rose_response = ""
    
    while True: 
        print(Fore.BLUE + "Listening...")
        secondary_query = STT()
        secondary_query = secondary_query.strip().lower()
        print(Fore.RESET + ">>> ", Fore.YELLOW + secondary_query)
            
        if any(word in secondary_query for word in input_lists.general):
            print("General...")
            ChatLogSaver.ChatLog(secondary_query, "...")
            continue
        
        elif secondary_query in input_lists.rose:
            print("About Rose...")
            rose_response = Chatbot_v2.aboutRose()
            ChatLogSaver.ChatLog(secondary_query, rose_response)
        
        elif secondary_query in input_lists.askingtime:
            print("Asking Time...")
            RealTimeQuery.telltime()
            
        elif any(q in secondary_query for q in input_lists.realTime):
            print("Real Time Query...")
            RealTimeQuery.RealTimeSearchExecuter(secondary_query)
        
        #AUTOMATIONS    
        
        elif "press" in secondary_query:
            print("Press key...")
            PressKeyFn(secondary_query)
              
        #YOUTUBE
        elif any(q in secondary_query for q in input_lists.youtube):
            print("Youtube query...")
            youtube.runYouTube(secondary_query)
        
        elif "manual search" in secondary_query or "search here" in secondary_query or "search in this tab" in secondary_query:
            new_query = secondary_query.replace("manual search", "").replace("search here", "").replace("search in this tab", "")
            youtube.yt_manual_search(new_query)

        elif secondary_query in input_lists.videoControls:
            print("Youtube video control...")
            video_controls.videoControl_executer(secondary_query)
            
        #SOCIAL MEDIA
        elif any(cmd in secondary_query for cmd in input_lists.social_media):
            print("Social Media...")
            SocialMedia_qm.social_media(secondary_query)
        
        elif "type message" in secondary_query or "type here" in secondary_query:
            print("Typing...")
            seamless_typing()

        #FILE EXPLORER
        elif any(cmd in secondary_query for cmd in input_lists.fileExplorer):
            print("File Explorer...")
            fileExplorer.fileEx(secondary_query)
        
        #APP CONTROL
        elif any(cmd in secondary_query for cmd in input_lists.automation_cmds):
            print("Automations...")
            AppControl(secondary_query)
            
        elif "battery" in secondary_query or "power status" in secondary_query:
            battery_status = RealTimeQuery.BatteryStatus().batteryStatus()
            TTS(battery_status)
            ChatLogSaver.ChatLog(secondary_query, battery_status)
            
        elif any(word in secondary_query for word in input_lists.turn_off):
            print("Sleeping...")
            initial.kill_frontend()
            TTS("You can call me anytime")
            exit()
            
        elif not any(qry in secondary_query for qry in input_lists.Chatbotless):
            print("Chatbot responsing...")
            rose_response = Chatbot_v2.get_response(secondary_query)
            ChatLogSaver.ChatLog(secondary_query, rose_response)
        
        else:
            print("I am unable to process the query.")
            TTS("I am unable to process the query.")

if __name__ == "__main__":

    scan = True
    # scan = FaceRecognition_v2().run_recog_v2()
    
    if scan:
        print(Fore.GREEN + "Initializing...")
        
        initial.initial_frontend()
        
        GreetMe()
        EnableRose()
        
    else:
        print("Say the passcode...")
        executing_query = STT()
        executing_query = executing_query.lower()
        print(">>> ", executing_query)
        
        if any(word in executing_query for word in input_lists.turn_on):
            print("Initializing...")
            GreetMe()
            EnableRose()