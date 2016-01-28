import datahuis

d = datahuis.huisdict

print "Hoi, ik woon op de %s samen met mijn moeder en zusje in %s. In het interieur zie je veel kleuren zoals %s" % (d['adres'], d['plaats'], d['kleuren'])
print "In het huis zitten %d deuren en %d ramen. " % (d['deuren'], d['ramen'])