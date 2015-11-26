# Esmee's work for Text IO 

## Homework
![Schets list]()

```
>>> couses = ['Photography', 'Design Philosophy', 'Media Theory', 'Design Research', 'Digital Media', 'Computer Skills', 'Graphic Design', 'Typography']
>>> print len(couses)
8
>>> couses.append(Media Theory lecture series)
  File "<stdin>", line 1
    couses.append(Media Theory lecture series)
                             ^
SyntaxError: invalid syntax
>>> couses.append(9)
>>> 9=[Media Theory lecture series]
  File "<stdin>", line 1
    9=[Media Theory lecture series]
                  ^
SyntaxError: invalid syntax
>>> couses.append(Media Theory lecture series)
  File "<stdin>", line 1
    couses.append(Media Theory lecture series)
                             ^
SyntaxError: invalid syntax
>>> print len(couses)
9
>>> couses.pop(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
>>> couses.pop()9
  File "<stdin>", line 1
    couses.pop()9
                ^
SyntaxError: invalid syntax
>>> couses.pop(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
>>> len(couses)
9

```
![List]()

```
>>> [0,1,2,3]
[0, 1, 2, 3]
>>> reeks = [0,1,2,3]
>>> reeks
[0, 1, 2, 3]
>>> naam= "Esmee"
>>> vakken= ["Photography", "Design Philosophy", "Media Theory", "Design Research", "Digital Media", "Computer Skills", "Graphic Design", "Typograhy"]
>>> vakken
['Photography', 'Design Philosophy', 'Media Theory', 'Design Research', 'Digital Media', 'Computer Skills', 'Graphic Design', 'Typograhy']
>>> len(vakken)
8
>>> vakken.pop()
'Typograhy'
>>> len (vakken)
7
>>> vakken.append("Typography")
>>> len(vakken)
8
>>> vakken.append("Media Theory Lectures")
>>> len(vakken)
9
>>> vakken.pop()
'Media Theory Lectures'
>>> len(vakken)
8
```
![Schets dictionaries]()

```
>>> heading ={}
>>> heading["adres"] = "Janthijssenstraat 13"
>>> heading["hoogte"] = "2.85m"
>>> heading["omtrek"] = "3.50m 2.80m"
>>> heading["deur"] = "1 deur"
>>> heading["raam"] = "1 raam"
>>> heading["kast"] = "4 kasten"
>>> print heading
{'omtrek': '3.50m 2.80m', 'raam': '1 raam', 'adres': 'Janthijssenstraat 13', 'kast': '4 kasten', 'deur': '1 deur', 'hoogte': '2.85m'}
```

![Dictionaries]()

```
>>> huis={'adres': "Janthijssenstraat 13", 'huisdier': 0, 'ramen': 21, 'deuren':8, 'kleuren': "blauw, grijs, zilver, wit, aqua, antraciet, paars, zwart"}
>>> huis
{'huisdier': 0, 'ramen': 21, 'kleuren': 'blauw, grijs, zilver, wit, aqua, antraciet, paars, zwart', 'adres': 'Janthijssenstraat 13', 'deuren': 8}
```

![Datastructure]()

```
Music = {
    'albums': [
        {
            'name': "A Night To Remember", 
            'singer': "Cyndi Lauper",
            'date': "1989",
            'tracks': [
                {
                    'track': "1-12",
                    'titel': "Intro",
                    'duur': "0:27"
                },
                {
                    'track': "2-12",
                    'titel': "I drove all night",
                    'duur': "4:11"
                },
                {
                    'track': "3-12",
                    'titel': "Primitive",
                    'duur': "3:48"
                },
                {
                    'track': "4-12",
                    'titel': "My first night without you",
                    'duur': "3:01"
                },
                {
                    'track': "5-12",
                    'titel': "Like a cat",
                    'duur': "3:23"
                },
                {
                    'track': "6-12",
                    'titel': "Heading west",
                    'duur': "3:54"
                },
                {
                    'track': "7-12",
                    'titel': "A night to remember",
                    'duur': "3:43"
                },
                {
                    'track': "8-12",
                    'titel': "Unconditional love",
                    'duur': "3:55"
                },
                {
                    'track': "9-12",
                    'titel': "Insecurious",
                    'duur': "3:31"
                },
                {
                    'track': "10-12",
                    'titel': "Dancing with a stranger",
                    'duur': "4:11"
                },
                {
                    'track': "11-12",
                    'titel': "I dont't want to be your friend",
                    'duur': "4:21"
                }
                {
                    'track': "12-12",
                    'titel': "Kindred spirit",
                    'duur': "1:16"
                }
                ]
        },
        {
            'name': "The Remixes", 
            'singer': "Shakira",
            'date': "1997",
            'tracks': [
                {
                    'track': "1-9",
                    'titel': "Shakira Dj memegamix",
                    'duur': "16:20"
                },
                {
                    'track': "2-9",
                    'titel': "Estoy aqui",
                    'duur': "9:32"
                },
                {
                    'track': "3-9",
                    'titel': "Donde estas corazon",
                    'duur': "8:48"
                },
                {
                    'track': "4-9",
                    'titel': "Un poco de amor",
                },
                {
                    'track': "5-9",
                    'titel': "Pies descalzos, suenos blancos",
                    'duur': "8:43"
                },
                {
                    'track':"6-9",
                    'titel': "Estoy aqui",
                    'duur':"6:06"
                },
                {
                    'track':"7-9",
                    'titel': "Donde estas corazon",
                    'duur':"6:44"
                },
                {
                    'track': "8-9",
                    'titel': "Un poco de amor",
                    'duur': "4:48"
                },
                {
                    'track': "9-9",
                    'titel': "Pies descalzos, suenos blancos",
                    'duur': "6:40"
                },
                ]
        },
        {
            'name': "The colour of my love", 
            'singer': "Celine Dion", 
            'date': "1993",
            'tracks': [
                {
                    'track': "1-15",
                    'titel': "The power of love"
                },
                {
                    'track': "2-15",
                    'titel': "Misled"
                },
                {
                    'track': "3-15",
                    'titel': "Think twice"
                },
                {
                    'track':"4-15",
                    'titel': "Only one road"
                },
                {
                    'track': "5-15",
                    'titel': "Everybody's talkin' my baby down"
                },
                {
                    'track': "6-15",
                    'titel': "Next plane out"
                },
                {
                    'track': "7-15",
                    'titel': "Real emotion"
                },
                {
                    'track': "8-15",
                    'titel': "When i fall in love (featured in the tristar motion picture)"                    
                },
                {
                    'track': "9-15",
                    'titel': "Love doesn't ask why"
                },
                {
                    'track':"10-15",
                    'titel': "Refuse to dance"
                },
                {
                    'track': "11-15",
                    'titel': "I remember L.A."
                },
                {
                    'track': "12-15",
                    'titel': "No living without loving you"
                },
                {
                    'track': "13-15",
                    'titel': "Lovin' proof"
                },
                {
                    'track': "14-15",
                    'titel': "Just walk away",
                },
                {
                    'track': "15-15",
                    'titel': "The colours of my love",
                }
                ]
        },
        ]
}

print 
```

![Gezamelijke opdracht]()

```
FontFamilie = {
    'Courier': [
        {
            'font varianten': [
                {
                    'naam':"Regular"
                },
                {
                    'naam':"Oblique"
                },
                {
                    'naam':"Bold"
                },
                {
                    'naam':"Bold Oblique"
                },
                
                ]
        },
    'Courier New': [
         {
            'font varianten': [
                {
                    'naam':"Regular"
                },
                {
                    'naam':"Italic"
                },
                {
                    'naam':"Bold"
                },
                {
                    'naam':"Bold Italic"
                },
                
                ]
        },
        ]
        {
            'Characters': [
                {
                    'Letters':"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'"
                },
                {
                    'Cijfers':"'0', 1', '2', '3', '4', '5', '6', '7', '8', '9'"
                },
                {
                    'Symbolen':"'±', '§', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '[', '}', ']', ':', ';', '"', ''', '\', '|', '<', ',', '>', '.', '/', '?', '~', '`'"
                },
                ]
        },
        { 
            'Glyphs': [
                {
                    'onderkast': "'å', 'à', 'é', 'ó', 'ò', 'ô', 'æ', 'ø'"
                },
                {
                    'Kapitalen': "'Å', 'À', 'É', 'Ó', 'Ò', 'Ô', 'Æ', 'Ø'"
                },
                ]
        },
        ]
}

```
## Concept

## Prototype: working demo

## Design the flow of the program

## How to use the script

## PDF format 
			
