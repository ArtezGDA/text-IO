#####import
```
Itunens = {
	'Caracal (Deluxe)': [
	{ 
		'artist': "Disclosure",
		'year':2015, 
		'songs': [
		{'title1': 'nocturnal', 'time': 6.44},
		{'title2': 'omen', 'time': 3.50},
		{'title3': 'holding on', 'time': 5.15},
		{'title4': 'willing & able', 'time': 4.52},
		{'title5': 'magnets', 'time': 3.19},
		{'title6': 'jaded', 'time': 4.33},
		{'title7': 'good itentions', 'time': 4.42},
		{'title8': 'superego', 'time': 4.33},
		{'title9': 'hourglass', 'time': 5.24},
		{'title10': 'echoes', 'time': 5.09},
		{'title11': 'masterpiece', 'time': 4.01},
		{'title12': 'molecules', 'time': 3.56},
		{'title13': 'moving mountains', 'time': 5.35},
		{'title14': 'bang that', 'time': 4.48},
		{'title15': 'afterthought', 'time': 5.20},
		]
	},

	
	],
}

```
```
import itunes.py 

d = Itunes.data

print "Mijn lievelings liedje is %s met de duur van %d minuten" % (d ['title14'], d ['time14'])
```
#####uitkomst
```
Last login: Wed Dec  9 14:49:38 on ttys001
[Nikki@MacBook-Pro-van-Nikki: ~]% cd/Users/Nikki/Documents/A\ School/Artez\ GD2A/Media\ Design/Zelf\ Text 
zsh: command not found: cd/Users/Nikki/Documents/A School/Artez GD2A/Media Design/Zelf Text
[Nikki@MacBook-Pro-van-Nikki: ~]% cd Documents                            [109]
[Nikki@MacBook-Pro-van-Nikki: ~/Documents]% cd /Users/Nikki/Documents/A\ School/Artez\ GD2A/Media\ Design/Zelf\ Text 
[Nikki@MacBook-Pro-van-Nikki: Artez GD2A/Media Design/Zelf Text]% python itunes_data.py
Traceback (most recent call last):
  File "itunes_data.py", line 1, in <module>
    import itunes.py 
  File "/Users/Nikki/Documents/A School/Artez GD2A/Media Design/Zelf Text/itunes.py", line 8
    {'title2': "omen', 'time": 3.50},
                             ^
SyntaxError: invalid syntax
[Nikki@MacBook-Pro-van-Nikki: Artez GD2A/Media Design/Zelf Text]% python itunes_data.py
Traceback (most recent call last):
  File "itunes_data.py", line 1, in <module>
    import itunes.py 
  File "/Users/Nikki/Documents/A School/Artez GD2A/Media Design/Zelf Text/itunes.py", line 8
    {'title2': "omen', 'time2": 3.50},
                              ^
SyntaxError: invalid syntax
[Nikki@MacBook-Pro-van-Nikki: Artez GD2A/Media Design/Zelf Text]%  
```