import webbrowser
# import pyautogui
# from Interactions.TextToSpeech import TTS
# from Interactions.SpeechToText import STT

messenger_chats = {
    "ammu": "https://www.facebook.com/messages/e2ee/t/7603999042978812",
    "abbu": "https://www.facebook.com/messages/e2ee/t/25382718241375779",
    "sanjida": "https://www.facebook.com/messages/e2ee/t/28648194188128166",
    "tarek": "https://www.facebook.com/messages/e2ee/t/7179858838705484",
    "nafis": "https://www.facebook.com/messages/e2ee/t/25859230327059133",
    "tushar": "https://www.facebook.com/messages/e2ee/t/6680737535380428",
    "shihab": "https://www.facebook.com/messages/e2ee/t/7832514523433369",
    "nafisa": "https://www.facebook.com/messages/e2ee/t/9201086119985785",
    "ridi apu": "https://www.facebook.com/messages/e2ee/t/7816531938371681",
    "gym": "https://www.facebook.com/messages/e2ee/t/8341676415849488"

}

messenger_groups = {
    "boys group": "https://www.facebook.com/messages/t/9100611343369787",
    "funcky group": "https://www.facebook.com/messages/t/7856081921117269",
    "chayer tong": "https://www.facebook.com/messages/t/24471371675786068",
    "team management": "https://www.facebook.com/messages/t/7106796946098252",
    "batch 2020": "https://www.facebook.com/messages/t/5874309452697797"
}

def messenger_chat(link):
    if str(link).startswith("https://www.facebook.com/messages/e2ee/t/"):
        webbrowser.open(link)
        
    else:
        print("Can't open the chat.")
        
def chat_finder(query):
    name = query.replace("open", "").replace("chat", "").replace("group", "").replace("messenger", "")
    
    for chat_name, chat_link in messenger_chats.items():
        if name.strip() in chat_name:
            messenger_chat(chat_link)

        
if __name__ == "__main__":
    n = input(": ")
    if "open messenger tashfi" in n:
        chat_finder(n)
        
    else:
        print("Failed")