import room1

d = room1.my_room

#print "Hello my name is", my_room['name'], "and I live at", my_room['address'],". The surface of my room is", my_room['surface'], "and my ceiling is", my_room['ceiling height'], "high. I have", my_room['windows'], "windows and", my_room['doors'], "door."

print "Hello, my name is %s, I live on the %s." (d['name'], d['address'])
print "My ceiling is %s high and the floor counts %s." (d['ceiling height'], d['surface'])
print "I have %d windows and %d door in my room." (d['windows'], d['doors'])

