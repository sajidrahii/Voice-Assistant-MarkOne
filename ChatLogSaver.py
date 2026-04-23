import json
import re

def ChatLog(my_query, rose_response):
    JSONPATH = r"Data\chatLog.json"
    
    clean_my_q =  re.sub(r"[^\w\s]", "", my_query)
    clean_rose_q = re.sub(r"[^\w\s]", "", rose_response)
    
    chat = {"me": f"{clean_my_q}", "rose": f"{clean_rose_q}"}
    
    try:
        with open(JSONPATH, "r") as j:
            prev_chat = json.load(j)
    
    except FileNotFoundError as e:
        print(e)
        prev_chat = []
        
    prev_chat.append(chat)
    
    try:
        with open(JSONPATH, "w") as j:
            json.dump(prev_chat, j, indent=4)
            print("Chatlog saved...")
    
    except FileNotFoundError as e:
        print("Failed to save chatlog", e)
        
if __name__ == "__main__":
    ChatLog("how are you?", "I am fine.")