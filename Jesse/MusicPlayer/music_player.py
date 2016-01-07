#!/usr/bin/python

# music_player.py

import json
import random
import subprocess
import os
import time

def randomMusic():
	jsonfile = "music.json"
	with open(jsonfile) as data_file:  #opent jsonfile
		data = json.load(data_file)

	return random.choice(data)  #random.choice = kiest willekeurig uit lijst van de jsonfile

def executeShell(notif_string, notif_title):
	applescript = 'display notification "%s" with title "%s"' % (notif_string, notif_title)  #"%s" is eigenlijk de naam die ik geef
	subprocess.call(["osascript", "-e", applescript])

def main():
	random_name = randomMusic()
	while True:
		executeShell(random_name, "MUSICPLAYER:")  #naam van mijn tool, staat in notificatie
		random_name = randomMusic()
		time.sleep(180)  # 180 zijn de seconden, dus 10 is 10 seconden

if __name__ == '__main__':
	main()