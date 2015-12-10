import room_file

d = room_file.room_sietske

print "Hello, my address is %s, %s in %s. " % (d['address'], d['postcode'], d['city'])
print "The height is %dm, the surface is %dm2, and it has %d door and %d windows" % (d['height ceiling'], d['surface'], d['doors'], d['windows'])
