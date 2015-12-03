# Anne's work for Text IO 

## Homework

Array 1

```
>>> [0, 1, 2, 3]
[0, 1, 2, 3]
>>> reeks = [0, 1, 2, 3]
>>> reeks
[0, 1, 2, 3]
>>> naam = "Anne"
>>> vakken = ["Media Design", "Fotografie"]
>>> vakken
['Media Design', 'Fotografie']
>>> len(vakken)
2
>>> vakken.append("Graphic Design")
>>> len(vakken)
3
>>> vakken.pop()
'Graphic Design'
>>> len(vakken)
2
>>> print len(vakken)
2
>>> vakken = vakken + ["Graphic Design", "Philosophy"]
>>> len(vakken)
4
>>> vakken.pop()
'Philosophy'
>>> vakken.pop()
'Graphic Design'
>>> vakken.pop()
'Fotografie'
>>> 

```
Dictionary 1

```
>>> kamer={}
>>> kamer["adres"] = "Bredestraat 7"
>>> kamer["hoogte"] = "2.60 m"
>>> kamer["breedte"] = "3.50 m"
>>> kamer["lengte"] = "6.25 m"
>>> kamer["omtrek"] = "3.50 m x 6.25 m =21.88 m"
>>> kamer["deur"] = "2 x deur"
>>> kamer["raam"] = "2 x raam"
>>> kamer["kast"] = "3 x kast"
>>> print kamer
{'omtrek': '3.50 m x 6.25 m =21.88 m', 'raam': '2 x raam', 'adres': 'Bredestraat 7', 'kast': '3 x kast', 'breedte': '3.50 m', 'deur': '2 x deur', 'hoogte': '2.60 m', 'lengte': '6.25 m'}
>>>
 
```
Dictionary 2 

```

>>> huis = {'adres': "Bredestraat 7", 'huisdieren': 1, 'huur': 235}
>>> huis
{'huur': 235, 'huisdieren': 1, 'adres': 'Bredestraat 7'}
>>> huis['huisdieren']
1
>>> huis['huur']
235
>>> def maalvijf(x):
...     return x * 5
... 
>>> maalvijf(2)
10
>>> huis['huisdieren']
1
>>> huis['huisdieren'] = 3
>>> huis['huisdieren']
3
>>> huis
{'huur': 235, 'huisdieren': 3, 'adres': 'Bredestraat 7'}
>>> 
>>> ['huisdieren'] 
['huisdieren']

```

Data structure I

	}
		
		Album = {
	
	'artist': 'Earth, Wind & Fire',
	'album': 'I Am',
	'date' : '1979',
	'total': '9 songs',

	}

		{

		'name': 'In the Stone',
		'duration': '4:48',
		'prize': '0,99',

		},

		{
		
		'name': 'Cant Let Go',
		'duration': '3:28',
		'prize': '1,29',

		},

		{
		
		'name': 'After the Love Has Gone',
		'duration': '4:38',
		'prize': '0,99',

		},
		
		{
		
		'name': 'Let your Feelings Show',
		'duration': '5:13',
		'prize': '0,99',

		
		},
		
		{
		
		'name': 'Boogie Wonderland (with The Emotions)',
		'duration': '4:48',
		'prize': '0,99',


		},
		
		{
		
		'name': 'Star',
		'duration': '4:25',
		'prize': '0,99',

		},

		{
		
		'name': 'Wait',
		'duration': '3:39',
		'prize': '0,99',

		},

		{
		
		'name': 'Rock That!',
		'duration': '3:07',
		'prize': '0,99',

		},

		{
		
		'name': 'You and I',
		'duration': '3:32',
		'prize': '1,29',

		}


Data structure II font

	Font= {
	
	'font': 'Proxima Nova',
	'designer': 'Mark Simonson',
	'date': '2005',
	'weights': '14',


		{

		'weight': 'Thin',

		},

		{
		
		'weight': 'Thin italic',

		},

		{
		
		'weight': 'Light',

		},

		{
		
		'weight': 'Light italic',

		},

		{
		
		'weight': 'Regular',

		},

		{
		
		'weight': 'Regular italic',

		},

		{
		
		'weight': 'Semibold',

		},

		{
		
		'weight': 'Semibold italic',

		},

		{
	
		'weight': 'Bold',

		},

		{
		
		'weight': 'Bold italic',

		},

		{

		'weight': 'Extrabold',

		},

		{
		
		'weight': 'Extrabold italic',

		},

		{
		
		'weight': 'Black',

		},

		{
		
		'weight': 'Black italic',

		}


	Characters= {
	
	'Proxima Nova': 'fontfamily',

	}

		{
		'Leestekens': '.' , ? / . < > + = _ - ( ) # @ ! | \ ~ ® $ % & ¤ £ ¦ § ¥ ± ⁕ ⁋ ⁜ ⁂ ⁘ ⁙ ⁖ ⁚ • • № ℗ ℻ √',

		},

		{
		'Glyphs': 'À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ú Ù Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ Ā ā Ă ă Ą ą Ć ć Ĉ ĉ Ċ ċ Č č Ď ď Đ đ Ē ē Ĕ ĕ Ė ė Ę ę Ě ě Ĝ ĝ Ğ ğ Ġ ġ Ģ ģ Ĥ ĥ Ħ ħ Ĩ ĩ Ī ī Ĭ ĭ Į į İ ı Ĳ ĳ Ĵ ĵ Ķ ķ ĸ Ĺ ĺ Ļ ļ Ľ ľ Ŀ ŀ Ł ł Ń ń Ņ ņ Ň ň ŉ Ŋ ŋ Ō ō Ŏ ŏ Ő ő Œ œ Ŕ ŕ Ŗ ŗ Ř ř Ś ś Ŝ ŝ Ş ş Š š Ţ ţ Ť ť Ŧ ŧ Ũ ũ Ū ū Ŭ ŭ Ů ů Ű ű Ų ų Ŵ ŵ Ŷ ŷ Ÿ Ź ź Ż ż Ž ž ſ ƀ Ƃ ƃ Ɖ Ƌ ƌ ƍ Ǝ Ə Ɛ Ƒ ƒ Ɩ Ɨ ƚ ƛ Ɲ ƞ Ɵ Ơ ơ Ʀ Ƨ ƨ Ʃ Ʈ Ư ư Ʊ Ƶ ƶ Ʒ Ƹ ƹ ƻ ǀ ǁ ǂ ǃ Ǆ ǅ ǆ Ǉ ǈ ǉ Ǌ ǋ ǌ Ǎ ǎ Ǐ ǐ Ǒ ǒ Ǔ ǔ Ǖ ǖ Ǘ ǘ Ǚ ǚ Ǜ ǜ ǝ Ǟ ǟ Ǡ ǡ ǣ Ǣ ǣ Ǥ ǥ ǿ Ǧ ǧ Ǩ ǩ Ǫ ǫ Ǭ ǭ Ǯ ǯ ǰ Ǳ ǲ ǳ Ǵ ǵ Ƿ Ǹ ǹ Ǻ ǻ Ǽ ǽ Ǿ ǿ Ȁ ȁ Ȃ ȃ Ȅ ȅ Ȇ ȇ Ȉ ȉ Ȋ ȋ Ȍ ȍ Ȏ ȏ Ȑ ȑ Ȓ ȓ Ȕ ȕ Ȗ ȗ Ș ș Ⱥ Ț ʬ ʡ ɸ ɚ Ɇ Ɋ',

		},

		{
		'Cijfers': 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 

		}
		
		


 



## Concept

## Prototype: working demo

## Design the flow of the program

## How to use the script

## PDF format 
			
