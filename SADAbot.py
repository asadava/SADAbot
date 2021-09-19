# These are the libraries I need to import for this.
import random
import time
import os
from gtts import gTTS

# This is the list of words used for the Schoolbot (School Auto Disciplinary Action Bot)
frontwords = ["Why are you such a ", "Why do you always act like a ", "You are a big, old ", "Can you please NOT be a ", "How in the world are you a ", "Somehow, you are a "]
badwords = ["newbie", "dummy", "noob", "horrible person", "uneducated weirdo", "weirdo", "fool", "fatty", "nerd", "dumb-o"]
endwords = ["? You can do better, but, no matter how hard you try, ", " when you are doing school? You can try to do better, but ", "? Seriously, get your act together, I beg of you, ", "during schooltime? You should be like your mother, but ", "? Your mom wasn't half as bad as you, " ". You are so dumb that insulting you is becoming boring, ", ". I genuinely thought you would be better, but "]
endierwords = ["you always are a ", "you know you won't achieve your goal, you ", "you are too busy being a ", "you can not stop acting like a ", "you can't stop being a ", "you are somehow still a"]
endsultwords = ["Minecraft piglin", "Big Mouth T.V. show bobble head", "Pizza Moncher 9000", "Chicken Little", "Minecraft witch", "Roblox 2006 character", "insult robot", "rubber duckie", "Chuck E Cheese mascot", "Minecraft enderman", "Minecraft endermite", "Captain Underpants", "Dumbo the Elephant"]
endsulkwords = [" looking ", " and a very fat ", " lookalike ", " disobedient ", ", whilst being a ", " exact lookalike ", " twin ", " acting ", " cosplaying ", " replacement ", " imitator "]

# This is the repeater, which completes the program! TIP: CLOSING THE PROGRAM WILL NOT END IT.
while True:

# This deletes the previous take, so that it's different every time.
    os.remove("LatestDiscipline.wav")

# This produces the voice for the bot, plays it, and plays the video.
    text = random.choice(frontwords) + random.choice(badwords) + random.choice(endwords) + random.choice(endierwords) + random.choice(endsultwords) + random.choice(endsulkwords) + random.choice(badwords)
    tts = gTTS(text, tld='com')
    tts.save("LatestDiscipline.wav")
    os.system("LatestDiscipline.wav")
    os.system("LipsyncDemo.mp4")

# This pauses the program for about another 30 seconds, counting the delay of every command.
    time.sleep(25)
