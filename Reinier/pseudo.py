inputText = getInputFromUser()
outputText = ""

characterToSelect = random.getint(0,len(inputText)-1)
timesToRepeat = random.getint(0,10)

for index in range(len(inputText)):
	if (index == characterToSelect)
		for secondIndex in range(timesToRepeat):
			outputText += inputText[index]
	else
		outputText += inputText[index]

print outputText