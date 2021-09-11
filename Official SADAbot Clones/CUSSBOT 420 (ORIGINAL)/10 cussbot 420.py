import os
from gtts import gTTS

text = "fuck shit haha penis"
tts = gTTS(text)
tts.save("Python\Cussbot\ppap.mp3")

import random
frontwords = ["You can suck my ", "You can lick my ", "Go eat a ", "Why are you such a "]
badwords = ["shit", "fuck", "cock", "shart", "hell", "damn", "dick", "bitch", "cunt", "penis"]
endwords = [", you turd monkey.", " and die.", ", but even the owner of said property won't let your ugly bum do it."]

print(random.choice(frontwords) + random.choice(badwords) + random.choice(endwords))