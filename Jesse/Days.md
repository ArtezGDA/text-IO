```
Last login: Mon Dec 21 11:39:56 on ttys000
[JesseWensing@admins-MBP: ~]% cd                                            [3]
[JesseWensing@admins-MBP: ~]% cd desktop                                    [4]
[JesseWensing@admins-MBP: ~/desktop]% ls                                    [5]
AFFICHES/
Bildschirmfoto 2015-12-08 um 10.34.35.png
Bildschirmfoto 2015-12-08 um 13.22.41.png
Bildschirmfoto 2015-12-10 um 16.30.28.png
GRAPHIC DESIGN HBO/
freeforallstuff/
gegevens huur/
kaartjes typo/
kaartjes.indd
kaartjes.pdf
kaartjes2.indd
map.ai*
maxresdefault-1.jpg
maxresdefault.jpg
posters graphic design/
text annie.docx
voorkant.ai*
zsh_testfiles.tar
[JesseWensing@admins-MBP: ~/desktop]% tar -xzf zsh_testfiles.tar            [6]
[JesseWensing@admins-MBP: ~/desktop]% cd Testfiles                          [7]
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% ls                          [8]
april.txt      friday.txt     march.txt      october.txt    thursday.txt
august.txt     january.txt    may.txt        saturday.txt   tuesday.txt
december.txt   july.txt       monday.txt     september.txt  wednesday.txt
february.txt   june.txt       november.txt   sunday.txt
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% mkdir Days                  [9]
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% ls                         [10]
Days/          february.txt   june.txt       november.txt   sunday.txt
april.txt      friday.txt     march.txt      october.txt    thursday.txt
august.txt     january.txt    may.txt        saturday.txt   tuesday.txt
december.txt   july.txt       monday.txt     september.txt  wednesday.txt
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% mv *day.txt                [11]
usage: mv [-f | -i | -n] [-v] source target
       mv [-f | -i | -n] [-v] source ... directory
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% mv *day.txt/Days           [12]
usage: mv [-f | -i | -n] [-v] source target
       mv [-f | -i | -n] [-v] source ... directory
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% ls                         [13]
Days/          february.txt   june.txt       november.txt   sunday.txt
april.txt      friday.txt     march.txt      october.txt    thursday.txt
august.txt     january.txt    may.txt        saturday.txt   tuesday.txt
december.txt   july.txt       monday.txt     september.txt  wednesday.txt
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% mv *day.txt Days           [14]
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% ls                         [15]
Days/          december.txt   july.txt       may.txt        september.txt
april.txt      february.txt   june.txt       november.txt
august.txt     january.txt    march.txt      october.txt
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% mkdir Months               [16]
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% mv *.txt Months            [17]
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% ls                         [18]
Days/   Months/
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% cat Months/*ember.txt      [19]
Month 12 is December
Month 11 is November
Month 9 is September
[JesseWensing@admins-MBP: ~/desktop/Testfiles]% brew install cowsay        [20]
zsh: command not found: brew
[JesseWensing@admins-MBP: ~/desktop/Testfiles]%     

```