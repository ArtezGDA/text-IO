#Dexter List

serie = {
	'seasons': [
		{
			'name': 'S01', 
			'year': 2006, 
			'director': "James Manos Jr.",
			'episodes': [
				{'name': 's01e01', 'title': "Pilot"},
				{'name': 's01e01', 'title': "Crocodile"},
				{'name': 's01e01', 'title': "Popping Cherry"},
				{'name': 's01e01', 'title': "Let's give the boy a hand"}
			]
		}, 
		{
			'name': 'S02', 
			'year': 2007, 
			'director': "James Manos Jr.",
			'episodes': [
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""}
			]
		}, 
		{
			'name': 'S03', 
			'year': 2008, 
			'director': "James Manos Jr.",
			'episodes': [
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""}
			]
		},  
		{
			'name': 'S04', 
			'year': 2009, 
			'director': "James Manos Jr.",
			'episodes': [
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""}
			]
		}, 
		{
			'name': 'S05', 
			'year': 2010, 
			'director': "James Manos Jr.",
			'episodes': [
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""}
			]
		}, 
		{
			'name': 'S06', 
			'year': 2011, 
			'director': "James Manos Jr.",
			'episodes': [
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""}
			]
		}, 
		{
			'name': 'S07', 
			'year': 2012, 
			'director': "James Manos Jr.",
			'episodes': [
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""}
			]
		},  
		{
			'name': 'S08', 
			'year': 2013, 
			'director': "James Manos Jr.",
			'episodes': [
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""},
				{'name': 's01e01', 'title': ""}
			]
		} 
	], 
	'main character': 'Dexter Morgan', 
	'title': 'Dexter'

#Dexter List 2
Last login: Thu Nov 19 13:47:30 on ttys001
MacBook-Pro-van-Niels-2:~ broersebroeder$ python
Python 2.7.10 (default, Aug 22 2015, 20:33:39) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> [0, 1, 2, 3]
[0, 1, 2, 3]
>>> reeks = [0, 1, 2, 3]
>>> reeks
[0, 1, 2, 3]
>>> len(reeks)
4
>>> reeks = ["wit", "blauw", "rood"]
>>> reeks
['wit', 'blauw', 'rood']
>>> len(reeks)
3
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> vakken
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'vakken' is not defined
>>> vakken = ["Media Design", "Photography", "Graphic Design"]
>>> vakken
['Media Design', 'Photography', 'Graphic Design']
>>> len(vakken)
3
>>> vakken.append("Typography")
>>> vakken
['Media Design', 'Photography', 'Graphic Design', 'Typography']
>>> len(vakken)
4
>>> l = [1, 2, 3]
>>> l
[1, 2, 3]
>>> l.type
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'type'
>>> t = (1, 2, 3)
>>> t
(1, 2, 3)
>>> t.type
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'type'
>>> t.append(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> t
(1, 2, 3)
>>> l.append(4)
>>> l
[1, 2, 3, 4]
>>> t
(1, 2, 3)
>>> vakken
['Media Design', 'Photography', 'Graphic Design', 'Typography']
>>> vakken[2]
'Graphic Design'
>>> vakken.pop
<built-in method pop of list object at 0x1046d7200>
>>> len(vakken)
4
>>> vakken.pop
<built-in method pop of list object at 0x1046d7200>
>>> vakken.pop()
'Typography'
>>> len(vakken)
3
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> huis = {'adres': "sonsbeeksingel 30", 'huisdieren': 1, 'huur': 297,25}
  File "<stdin>", line 1
    huis = {'adres': "sonsbeeksingel 30", 'huisdieren': 1, 'huur': 297,25}
                                                                         ^
SyntaxError: invalid syntax
>>> huis = {'adres': "sonsbeeksingel 30", 'huisdieren': 1, 'huur': 297,25}
  File "<stdin>", line 1
    huis = {'adres': "sonsbeeksingel 30", 'huisdieren': 1, 'huur': 297,25}
                                                                         ^
SyntaxError: invalid syntax
>>> huis
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'huis' is not defined
>>> huis = {'adres': "Sonsbeeksingel 30", 'huisdieren': 1, 'huur': 297.25}
>>> huis
{'huur': 297.25, 'huisdieren': 1, 'adres': 'Sonsbeeksingel 30'}
>>> huis['huisdieren']
1
>>> "Ik woon op de %s, en heb %d huisdieren" % (huis['adres'], huis['huisdieren'])
'Ik woon op de Sonsbeeksingel 30, en heb 1 huisdieren'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> huis['huisdieren']
1
>>> huis['huisdieren'] = ['Max']
>>> huis
{'huur': 297.25, 'huisdieren': ['Max'], 'adres': 'Sonsbeeksingel 30'}
>>> 
>>> 
>>> 
>>> serie = {'title': "Dexter", 'main character': "Dexter Morgan"}
>>> serie['seasons'] = 9
>>> serie
{'seasons': 9, 'main character': 'Dexter Morgan', 'title': 'Dexter'}
>>> 
>>> serie['seasons'] = 8
>>> serie
{'seasons': 8, 'main character': 'Dexter Morgan', 'title': 'Dexter'}
>>> 
>>> serie = {'seasons': ['s01', 's02', 's03'], 'main character': 'Dexter Morgan', 'title': 'Dexter']]
  File "<stdin>", line 1
    serie = {'seasons': ['s01', 's02', 's03'], 'main character': 'Dexter Morgan', 'title': 'Dexter']]
                                                                                                   ^
SyntaxError: invalid syntax
>>> serie = {'seasons': ['s01', 's02', 's03'], 'main character': 'Dexter Morgan', 'title': 'Dexter']}
  File "<stdin>", line 1
    serie = {'seasons': ['s01', 's02', 's03'], 'main character': 'Dexter Morgan', 'title': 'Dexter']}
                                                                                                   ^
SyntaxError: invalid syntax
>>> 