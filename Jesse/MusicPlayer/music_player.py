#!/usr/bin/python

# music_player.py

import json
import random
import subprocess
import os
import time

def randomMusic():
	jsonfile = "music.json"
	with open(jsonfile) as data_file:
		data = json.load(data_file)

	return random.choice(data)

def executeShell(notif_string, notif_title):
	applescript = 'display notification "%s" with title "%s"' % (notif_string, notif_title)
	subprocess.call(["osascript", "-e", applescript])

def main():
	random_name = randomMusic()
	while True:
		executeShell(random_name, "MUSICPLAYER:")
		random_name = randomMusic()
		time.sleep(180)

if __name__ == '__main__':
	main()