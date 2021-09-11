# These are the libraries I need to import for this.
import random
import time
import os
from gtts import gTTS

# This is the list of words used for the Schoolbot (School Auto Disciplinary Action Bot)
frontwords = ["Why are you such a ", "Why do you always act like a ", "You are a big, old ", "Can you please NOT be a ", "How in the world are you a", "Somehow, you are a "]
badwords = ["newbie", "dummy", "noob", "horrible person", "uneducated weirdo", "weirdo", "fool", "fatty", "nerd"]
endwords = ["? You can do better, but, no matter how hard you try, ", " when you are doing school? You can try to do better, but ", "? Seriously, get your act together, I beg of you, ", "during schooltime? You should be like your mother, but ", "? Your mom wasn't half as bad as you, " ". You are so dumb that insulting you is becoming boring, "]
endierwords = ["you always are a ", "you know you won't achieve your goal, you ", "you are too busy being a ", "you can not stop acting like a "]
endsultwords = ["Minecraft Piglin looking ", "Big Mouth T.V. show bobble head looking ", "Pizza Moncher 9000 and a very fat ", "Chicken Little lookalike, whilst being a ", "disobedient prick ", "Minecraft Witch exact lookalike"]

# This is the repeater, which completes the program! TIP: CLOSING THE PROGRAM WILL NOT END IT.
while True:

# This deletes the previous take, so that it's different every time.
    os.remove("Python\Schoolbot\LatestDiscipline.wav")

# This produces the voice for the bot.
    text = random.choice(frontwords) + random.choice(badwords) + random.choice(endwords) + random.choice(endierwords) + random.choice(endsultwords) + random.choice(badwords)
    tts = gTTS(text, tld='com')
    tts.save("Python\Schoolbot\LatestDiscipline.wav")

# This plays the audio file.
    os.system("Python\Schoolbot\LatestDiscipline.wav")

# This pauses the program for about another 30 seconds, counting the delay of every command.
    time.sleep(25)