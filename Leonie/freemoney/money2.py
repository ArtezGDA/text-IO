import dollar

#defining the functions
txt = "twerk"
output = [ "", "", "", "", ""]

# char = p

font = dollar.font

#making a loop to make sure all the letters will be placed in a scentence next to eachother
for char in txt:
	for i in range(5):
		output[i] = output[i] + font[char][i]


#Printing the letters
for i in range(5):
	print output[i]