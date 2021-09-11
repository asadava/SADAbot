# These are the libraries I need to import for this.
import random
import time
import os
from gtts import gTTS

# This asks you for your name, and adds it to a variable.
name = input("Enter your name!")

# This is the list of words used for the PISAbot! (Pizza Indulging and Scarfing Accomplice bot.)
frontwords = ["C\'mon, " + name + ", give it your all! You can eat this ", "Remember " + name + ", you can devour this ", "Don't forget that you can start eating this"]
nicewords = ["fresh pepperoni pizza", "cheese pizza", "pineapple pizza", "cheese alfredo pizza", "New York styled pizza", "fresh cheese pizza", "pepperoni and mushrooms pizza"]
endwords = [" in just one bite!", " very quickly!", " right after this ad from our sponsor:,", " faster than Sonic the Hedgehog or the Flash ever could!"]

#This is the (simple) repeater, which completes the program! TIP: CLOSING THE PROGRAM WILL NOT END IT.
while True:

#This deletes the previous take, so that it's different every time.
    os.remove("Python\PISAbot\LatestEncouragement.wav")

# This produces the voice for the bot.
    text = random.choice(frontwords) + random.choice(nicewords) + random.choice(endwords)
    tts = gTTS(text, tld='com')
    tts.save("Python\PISAbot\LatestEncouragement.wav")

# This plays the audio file.
    os.system("Python\PISAbot\LatestEncouragement.wav")

# This pauses the program for about another 30 seconds, counting the delay of every command.
    time.sleep(25)