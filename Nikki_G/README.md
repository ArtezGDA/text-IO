# Nikki G's work for Text IO 

## Homework
[collections]() (python code)

###Cowsay

```
Last login: Thu Dec  3 13:44:04 on ttys000
[Nikki@MacBook-Pro-van-Nikki: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
It appears Homebrew is already installed. If your intent is to reinstall you
should do the following before running this installer again:
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
The current contents of /usr/local are bin Cellar clamXav CODEOFCONDUCT.md CONTRIBUTING.md Library LICENSE.txt opt README.md share SUPPORTERS.md .git .gitignore
[Nikki@MacBook-Pro-van-Nikki: ~]% cowsay "Hoi"                             [73]
 _____ 
< Hoi >
 ----- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
[Nikki@MacBook-Pro-van-Nikki: ~]% cowsay -f stegosaurus "Hoi"              [74]
 _____ 
< Hoi >
 ----- 
\                             .       .
 \                           / `.   .' " 
  \                  .---.  <    > <    >  .---.
   \                 |    \  \ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \~~~\.'                    `./~~~/
       ---------   \__/                        \__/
      .'  O    \     /               /       \  " 
     (_____,    `._.'               |         }  \/~~~/
      `----.          /       }     |        /    \__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>
[Nikki@MacBook-Pro-van-Nikki: ~]% 

```

### Array
```
a = ["Filosofie", "Fotografie", "Design Reaserch", "Annie", "Computer Skills", "Media Design", "Typografie", "Grafisch"]
print len(a)

a + ["Media Theorie"]

#a.append("Media Theorie")

print len (a)

a.pop(7)
print len (a)

a.pop(3)
print len (a)

print a[4]


print a
```

###Dictonairy
```
d = { 'adres':19, 'oppervlakte kamer': "21 m2", 'hoogte kamer': "3,2 m", 'bedgrootte': "2persoons 160cm bij 200 cm", 'merk printer': "Epson XP-950"}

print 'adres'    
```


### Poe
```
"Last login: Wed Dec  2 13:22:37 on ttys000
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   313k      0  0:00:01  0:00:01 --:--:--  
[Nikki@MacBook-Pro-van-Nikki: ~]% curl http://www.gutenberg.org/files/2148/2148-8.txt > vol2.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   313k      0  0:00:01  0:00:01 --:--:--  313k 313k
[Nikki@MacBook-Pro-van-Nikki: ~]% curl http://www.gutenberg.org/files/2149/2149-8.txt > vol3.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   313k      0  0:00:01  0:00:01 --:--:--  313k
[Nikki@MacBook-Pro-van-Nikki: ~]% curl http://www.gutenberg.org/files/2147/2147-8.txt > vol4.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   313k      0  0:00:01  0:00:01 --:--:--  313k
[Nikki@MacBook-Pro-van-Nikki: ~]% curl http://www.gutenberg.org/files/2147/2147-8.txt > vol5.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   313k      0  0:00:01  0:00:01 --:--:--  313k


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


kamer = {
	'kamer': [
	{
		'plaats': "Arnhem", 
		'straat naam': 'Kastanjelaan 17' , 
		'postcode': '6828 GH',
		'huisnummer':17,
	},

	{
		'opp':21 ,
		'hoogte':3.10 , 
		'lengte':3.50 , 
		'breedte':6, 
	},

	{
		'interieur': [
			{'banken':0 },
			{'bureaus': 1 },
			{'kasten': 1},
			{'deur': 2 },
			{'ramen': 2},
			]
	},
	
	],

	}


## Concept

## Prototype: working demo

## Design the flow of the program

## How to use the script

## PDF format 
			