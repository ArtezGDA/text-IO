import dictionary_kamer

d = dictionary_kamer.dict

print "Het adres van %s's kamer is in %s, %s %d, %s. " % (d['naam'],d['stad'],d['straat'],d['nummer'],d['postcode'],)
print "De kamer heeft %d kamers en er wonen %d huisdieren. " % (d['kamers'],d['huisdieren'])