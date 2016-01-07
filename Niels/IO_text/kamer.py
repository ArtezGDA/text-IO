d = {

'plaats': "Arnhem",
'straat naam': "Sonsbeeksingel 30" ,
'postcode': "6814 AB",
'huisnummer':30,
'opp':11.5 ,
'hoogte':3.77 ,
'lengte':3.77 ,
'breedte':3.05,
'bureaus': 1 ,
'kasten': 3,
'deur': 1 ,
'ramen': 1,
'bed': 1,

}

print d
print d['plaats']
zin = "I live in %s on the street %s, the postcode is %s and my number is %s. The squaremeters of my room are %s m2, his height is %s m, his length is %s m and his width is %s m. My room contains %s desk, %s closets, %s door, %s window and %s bed." % (d ["plaats"], d ["straat naam"], d ["postcode"], d ["huisnummer"], d ["opp"], d ["hoogte"], d ["lengte"], d ["breedte"], d ["bureaus"], d ["kasten"], d ["deur"], d ["ramen"], d ["bed"])
print zin