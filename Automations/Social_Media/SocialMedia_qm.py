from Automations.Social_Media.messenger import chat_finder

def social_media(query):
    if (word in query for word in ["messenger", "chat"]):
        chat_finder(query)