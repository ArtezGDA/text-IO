import data_kth

d = data_kth.dict

print "The Adress of %s's room is in %s, %s %d, %s. " % (d['name'],d['city'],d['adress'],d['number'],d['postcode'],)
print "My room is approximately %d big and the ceiling is %d high. " % (d['roomsize'],d['ceilingheight'])
print "On top of that I have %d window, and %d door" % (d['windows'],d['doors'], )

