import datahuis

d = datahuis.huisdict

print "Hoi, ik woon op de %s samen met mijn moeder en zusje. We hebben % huisdieren. In het huis zitten % deuren en % ramen. In het interieur zie je veel kleuren zoals % " % (d['adres'], d['huisdieren'], d['deuren'], d['ramen'], d['kleuren'])