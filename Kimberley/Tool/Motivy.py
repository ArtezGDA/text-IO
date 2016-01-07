#!/usr/bin/python
# Motivy.py
# (c) 2015 Artez Graphic Design Arnhem / Kimberley ter Heerdt GDA2B
# Motivy.py

"""Motivy provides you every 15 min of motivational messages such as Good Job!,
You can do this!,Awesome!. These messages will be seen through a Note of the 
Notification center so they will pop-up immediately every 15 min."""

import json
import random
import subprocess
import threading

jsonfile = "Motivyinput.json"  # Selects JSON file for input
minutes = 15  # Minutes inbetween the Notifications

with open(jsonfile, "r") as file:
    "Opens and loads Motivyinput JSON file into the python file. The JSON file will be used in the def notify to put the text into the applescript"
    data = json.load(file)

def notify():
    "selects information from a range of the two lists in the motivyinput JSON file, puts it into an osascript to  "
    random_text = random.choice(data["text"]) # Name of the Notification = Motivy
    random_subtitle = random.choice(data["soundname"]) # a function to pick a random soundname from the soundname list in the JSON file and puts it in the Notification as an subtitle
    random_soundname = random.choice(data["soundname"]) # a function to pick a random soundname from the soundname list in the JSON file and searches this in your computer to use it as a notification sound
    subprocess.call(["osascript", "-e", "display notification \"{0}\" with title \"{1}\" subtitle \"{2}\"  sound name \"{3}\"".format(random_text, "Motivy", random_soundname,random_soundname)])

def repeat():
  "makes a repetition out of the script and calls the minutes that are "
  threading.Timer(minutes*60, repeat).start() # calls minutes above devides it into 60(seconds) and says it needs to repeat the code after the 15 minutes.
  notify()
  

repeat() # When script is done, repeat script again"
