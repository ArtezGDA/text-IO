import bier

d = bier.reclamedict

print "Supermark %s, %s heb je met %s korting." % (d['plaats'], d['hoeveel'], d['korting'])
print "Het is ongeveer %d liter, normaal voor %d euro en deze week voor %d euro. " % (d['liter'], d['normaal'], d['deze week'])