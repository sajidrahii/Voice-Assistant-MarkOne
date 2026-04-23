from dotenv import dotenv_values
env_vars = dotenv_values(".env")
markname = env_vars.get("MarkedName")

#LIBRARIES
turn_on = [str(markname).lower(), "wake", "wake up", "start", "are you there"]
turn_off = ["sleep", "go to sleep", "turn off", "off", "stop", "exit"]
general = ["ah", "oh", "i see", "ok", "i got that", "alright"]

automation_cmds = ["start", "open", "close", "shut", "turn off", "off"]

rose = [
    "yourself",
    "tell me about yourself",
    "who are you",
    "what are you"
]

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
    "google search",
    "google",
    "search on wikipedia",
    "check on wikipedia",
    "wikipedia",
    "facebook search",
    "search on facebook",
    "look for",
    "who",
    "who is",
    "tell me who is",
    "tell me about"
]

youtube = [
    "play on youtube", "youtube", "youtube play"
    "search youtube", "youtube search", "searh on youtube"
]

videoControls = [
    "play video", "pause", "resume", "continue", "mute", "unmute", "minimize", "maximize",
    "seek forward", "play forward", "seek back", "seek backward", "forward", "backward",
    "volume up", "volume down", "go to home", "speed up", "slow down", "caption on", "caption off", "subtitle"             
]

fileExplorer = [
    "show movies", "movie list", "play movie", "show movies", "show all movies"
] 

social_media = ["open messenger", "open chat", "open group chat"]

Chatbotless = (
    rose + realTime + automation_cmds +
    askingtime + turn_on + turn_off + 
    videoControls
)
