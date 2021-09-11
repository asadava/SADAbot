# These are the libraries I need to import for this.
import random
import time
import os
from gtts import gTTS

# This is the list of words used for the Schoolbot (School Auto Disciplinary Action Bot)
frontwords = ["Why are you such a ", "Why do you always act like a ", "You are a big, old ", "Can you please NOT be a ", "How in the world are you a"]
badwords = ["newbie", "dummy", "noob", "horrible person", "uneducated weirdo", "weirdo", "fool"]
endwords = [" at school? You can do better, but, no matter how hard you try, ", " when you are doing school? You can try to do better, but ", " at school? Seriously, get your act together, you ", "during schooltime? You should be like your mother, but you are too ugly to be like her.", " during school? No one loves you anymore, you big and dense bean burrito."]
endierwords = ["you always fail.", "byou know you won't achieve your goal.", ""]
endsultwords = ["Minecraft Piglin looking ", "Big Mouth T.V. show looking head.", "Pizza Moncher 9000."]

#This is the repeater, which completes the program! TIP: CLOSING THE PROGRAM WILL NOT END IT.
while True:

#This deletes the previous take, so that it's different every time.
    os.remove("Python\Schoolbot\LatestDiscipline.wav")

# This produces the voice for the bot.
    text = random.choice(frontwords) + random.choice(badwords) + random.choice(endwords) + random.choice(endierwords)
    tts = gTTS(text)
    tts.save("Python\Schoolbot\LatestDiscipline.wav")

# This plays the audio file.
    os.system("Python\Schoolbot\LatestDiscipline.wav")

# This pauses the program for about another 30 seconds, counting the delay of every command.
    time.sleep(25)