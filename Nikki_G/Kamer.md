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