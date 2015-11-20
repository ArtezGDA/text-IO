```
size(512, 512)
background(1)

lessen = ["Computerskills", "Design & Philosophy", "Design Research", "Digital Media", "Graphic Design", "Media & Design Theory", "Photography", "Time Based Media", "Typography"]

print len(lessen) #print de aantal lessen op de lijst uit
print lessen[3] #print de vierde les (de eerste les is 0)
print lessen #print de nieuwe lijst van de lessen
lessen.append("Media Theory Lectures") #voeg een nieuwe les toe aan de lijst'Media Theory Lectures'.
print lessen #print de nieuwe lijst van de lessen
del lessen[9] #verwijder les negen 'Media Theory Lectures'
print lessen #print de nieuwe lijst van de lessen
lessen.insert(4, "Media Theory Lectures") 

```