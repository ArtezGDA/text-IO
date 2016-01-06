#!/usr/bin/python

# random_notifs.py

import json
import random
import subprocess

def randomLine():
	jsonfile = "text.json"
	with open(jsonfile) as data_file:
		data = json.load(data_file)

#print complete text in random order

		