```
import data_kth

d = data_kth.dict

print "The Adress of %s's room is in %s, %s %d, %s. " % (d['name'],d['city'],d['adress'],d['number'],d['postcode'],)
print "My room is approximately %d big and the ceiling is %d high. " % (d['roomsize'],d['ceilingheight'])
print "On top of that I have %d window, and %d door" % (d['windows'],d['doors'], )


import data_shirin

d = data_shirin.my_dict

print "In Comparison to my friends %s's room that is in %s, %s %d. " % (d['name'],d['city'],d['adress'],d['number'],)
print "Her room is approximately %d big and the ceiling is also %d high. " % (d['roomsize'],d['ceilingheight'])
print "She has %d windows, and also %d door." % (d['windows'],d['doors'], )


```