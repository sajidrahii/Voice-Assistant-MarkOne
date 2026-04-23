import speech_recognition as sr
# import pyttsx3
from colorama import Fore

r = sr.Recognizer()

def STT():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                
                return MyText
                
        except sr.RequestError as e:
            print(f"Could not request result: {e}".format(e))
            
        except sr.UnknownValueError:
            print(Fore.RED + "Can't hear...")
            

# def output_text(text):
#     with open(r"Data\output_text.txt", "a") as f: 
#         f.write(text + "\n")
#         f.close()
    
    # return

if __name__ == "__main__":
    while True:
        text = STT()
        # output_text(text)

        print(">>> ", text)
        
        if text == "exit":
            exit()