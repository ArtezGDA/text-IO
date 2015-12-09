```
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
```	

```
d = {
    
		'plaats': "Arnhem", 
		'straat naam': "Kastanjelaan 17" , 
		'postcode': "6828 GH",
		'huisnummer':17,
		'opp':21 ,
		'hoogte':3.10 , 
		'lengte':3.50 , 
		'breedte':6,
		'banken':0 ,
	    'bureaus': 1 ,
		'kasten': 1,
		'deur': 2 ,
		'ramen': 2,
	    'bed': 1,
		
	}

print d
print d['plaats']
zin = "i live in %s on the street %s, the postcode is %s" % (d ["plaats"], d ["straat naam"], d ["postcode"])
print zin


```
####Goed
```
my_room = {
    
		'plaats': "Arnhem", 
		'straat naam': "Kastanjelaan 17" , 
		'postcode': "6828 GH",
		'huisnummer':17,
		'opp':21 ,
		'hoogte':3.10 , 
		'lengte':3.50 , 
		'breedte':6,
		'banken':0 ,
	    'bureaus': 1 ,
		'kasten': 1,
		'deur': 2 ,
		'ramen': 2,
	    'bed': 1,
		
	}
	
```	
####terminal
```
import my_data

d = my_data. my_room

print "i live in %s on the street %s, the postcode is %s, the opp is %d. The height of my room is %d, the length of my room is %d, the room has a width of %d, the room has %d " % (d ["plaats"], d ["straat naam"], d ["postcode"] , d ["opp"] , d ["hoogte"] , d ["lengte"] , d ["breedte"] , d ["banken"])
```