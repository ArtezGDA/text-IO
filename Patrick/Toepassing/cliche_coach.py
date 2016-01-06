#!/usr/bin/python

# cliche_coach.py

import json
import random
import subprocess
import os
import time

def randomZin():
	jsonfile = "zinnen.json"
	with open(jsonfile) as data_file:
		data = json.load(data_file)

	return random.choice(data)

def executeShell(notif_string, notif_title):
	applescript = 'display notification "%s" with title "%s"' % (notif_string, notif_title)
	subprocess.call(["osascript", "-e", applescript])

def main():
	random_name = randomZin()
	while True:
		executeShell(random_name, "COACH:")
		random_name = randomZin()
		time.sleep(60)

if __name__ == '__main__':
	main()