import my_data_file

d = my_data_file.my_data

print "i live in %s on the street %s, the postcode is %s, the surface is %d. The height of my room is %d, the length of my room is %d, the room has a width of %d, the room has %d " % (d ["plaats"], d ["straat naam"], d ["postcode"] , d ["surface"] , d ["hoogte"] , d ["lengte"] , d ["breedte"] , d ["banken"])