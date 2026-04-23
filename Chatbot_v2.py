#if can't answer it will ask for a reply

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import pandas as pd
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import random
from dotenv import dotenv_values

from Interactions.TextToSpeech import TTS
from Interactions.SpeechToText import STT

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

env_vars = dotenv_values(".env")
Assistantname = env_vars.get("MarkedName")
Username = env_vars.get("Username")

questions = [
    "how are you",
    "how is going on",
    "how is going",
    "what is up",
    "what's up"
]  
    
rose = [
    "tell me about yourself",
    "who are you",
    "what are you"
]

def greetingsConv():
    
    answers = [
        "i am running at my prototype state",
        "i am fine, how may i help you",
        "i am at improvement state"
    ]
    
    reply = random.choice(answers)
    print(reply)
    TTS(reply)
    
    return reply
    
def aboutRose():
    answer = f"I am {Assistantname}, a voice assistant created by Mr.{Username} and I help to do some task with the help of voice command."
    print(answer)
    TTS(answer)
    
    return answer

def preprocess(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    tokens = word_tokenize(text)
    return " ".join([lemmatizer.lemmatize(token) for token in tokens])

# Load data
try:
    with open(r"Data\conversations.json", "r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

df = pd.DataFrame(data)

# Handle empty data
if df.empty:
    df = pd.DataFrame(columns=["input", "output"])

df['processed_input'] = df['input'].apply(preprocess)
df['processed_output'] = df['output'].apply(preprocess)

# Save processed data (optional)
df.to_json(r'Data\processed_data.json', indent=4)

# MODEL
vectorizer = TfidfVectorizer()

if not df.empty:
    X = vectorizer.fit_transform(df['processed_input'])
else:
    X = None

def get_response(user_input):
    global X, vectorizer, df
    
    input_processed = preprocess(user_input)

    if X is None or X.shape[0] == 0:
        print("No data to compare with yet.")
        return

    input_vec = vectorizer.transform([input_processed])
    similarities = cosine_similarity(input_vec, X)
    best_score = similarities.max()
    best_match_idx = similarities.argmax()

    if best_score > 0.6:  # similarity threshold
        # return df.iloc[best_match_idx]["output"]
        TTS(df.iloc[best_match_idx]["output"])
    
    else:
        print("I don't have the answer to this query at this moment.")
        TTS("I don't have the answer to this query at this moment.")
        # suggest_in = STT()
        # suggest = suggest_in.strip().lower()

        # if suggest == "yes":
        #     print("Your suggestion: ")
        #     user_answer = STT()
            
        #     general_pre_words = [
        #         "well you can say ",
        #         "you can say ",
        #         "you should say ",
        #         "the answer can be ",
        #         "the answer is "
        #     ]
            
        #     user_answer = user_answer.replace(str(any(pre_w in user_answer for pre_w in general_pre_words)), "")

        #     # Append to original data list
        #     new_entry = {"input": user_input, "output": user_answer}
        #     data.append(new_entry)

        #     # Save back to file
        #     with open(r"Data\conversations.json", "w") as f:
        #         json.dump(data, f, indent=4)

        #     print("Thanks you for your feedback.")
        #     TTS("Thank you for your feedback.")

        #     # Update model
        #     df.loc[len(df)] = [user_input, user_answer, preprocess(user_input), preprocess(user_answer)]
        #     X = vectorizer.fit_transform(df["processed_input"])
            
        # else:
        #     print("Thank you for your feedback.")
        #     TTS("Thank you for your feedback.") 
        #     pass 
    
    return df.iloc[best_match_idx]["output"]
        

# SAVE MODEL
with open(r"Data\tfidf_model.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

if __name__ == "__main__":
    while True:
        user_input = STT()
        print("Me: ", user_input)
        
        if user_input.lower() == "exit":
            print("Exiting...")
            break
        
        response = get_response(user_input)
        
        if response:
            print("Rose:", response)
            # TTS(response)
 