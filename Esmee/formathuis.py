import datahuis

d = datahuis.huisdict

print "Hoi, ik woon op de %s samen met mijn moeder en zusje in %s. " % (d['addres'], d['plaats'])
print "In het huis zitten %d deuren en %d ramen. In het interieur zie je veel kleuren zoals %d " % (d['deuren'], d['ramen'], d['kleuren'])