#!/usr/bin/python

#joke.generator.py

"""Import random and database.py in order to use these two in the code"""

#import the random function to allow the code to choose randomly from the database
import random
#importing the database which contains all the content
import database


def main():
	"""Opens the files deliverd to this script
	and print the first line.
	"""
	#call the list of strings within the database and in order to shorten, translate it into a variable
	j = database.list
	#print out randomly strings from the database
	print random.choice(j)
	#
	
if __name__ == '__main__':
	main()