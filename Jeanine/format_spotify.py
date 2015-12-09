import my_data_file_spotify

d = my_data_file_spotify.my_data_spotify 

print "My favorite song from the album %s is %s, but my all time favorite song is %s." % (d['Album'], d['Track'], d['Track'])

# maar hoe kun je nou aangeven welk liedje hij moet pakken?