#Apace leaflet
##Desc

Ever need a quick list from offers from the supermarket? You have to look at offers from the supermarketIn a student's life you have to be thrifty with your pennies. Maybe you just need him to give you some quick advice. Yodaism is a collection of quotes and some ascii porn to get your Yoda fix.


##Table of Contents
Install</br>
Setup</br>
Usage</br>
License</br>

##Install

pip install terminaltables

##How-to

There is really only two modes right now for it.

To get just a plain quote just execute the gem with no options

[~/yoda]$ yodaism
..........
To get a picture of yoda in ascii format

[~/yoda]$ yodaism ascii
..........
Voorbeeld

That's all there is, very simple.

##Use it in your script

require 'yodaism'

class YodaQuote
    include Yodaism

	from terminaltables import AsciiTable
	table_data = [
    ['Heading1', 'Heading2'],
    ['row1 column1', 'row1 column2'],
    ['row2 column1', 'row2 column2']
	]
	table = AsciiTable(table_data)
	print table.table
	+--------------+--------------+
	| Heading1     | Heading2     |
	+--------------+--------------+
	| row1 column1 | row1 column2 |
	| row2 column1 | row2 column2 |
	+--------------+--------------+
	end

example = test.py
puts example.ascii
puts example.random

##License (MIT License)

Apeace Leaflet is released under the MIT license.

Copyright © 2016 Esmee Ellson 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

![3 conversaties](screenshot2.jpg)
![3 conversaties](screenshot.jpg)

Write proper documentation for your tool:
In the README.md describe all the neccessary elements of documentation:
What your tool is and what it does
How to install your tool
Screenshots of your tool
Examples how to use your tool
Dependencies on other tools / python modules


