```
my_data_file.py
```
```
my_room = {
		'plaats': "Herveld", 
		'straat naam': "Mercurius 4" , 
		'postcode': "6674 EC",
		'huisnummer': 4,
		'surface': 24,
		'hoogte': 3, 
		'lengte': 4, 
		'breedte': 6,
		'banken': 1,
	    'bureaus': 1,
		'kasten': 1,
		'deur': 1,
		'ramen': 3,
	    'bed': 1,
		}
```
```
format.py
```
```
import my_data_file

d = my_data_file.my_data

print "i live in %s on the street %s, the postcode is %s, the surface is %d. The height of my room is %d, the length of my room is %d, the room has a width of %d, the room has %d " % (d ["plaats"], d ["straat naam"], d ["postcode"] , d ["surface"] , d ["hoogte"] , d ["lengte"] , d ["breedte"] , d ["banken"])
```