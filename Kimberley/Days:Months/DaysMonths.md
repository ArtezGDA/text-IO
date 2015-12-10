```
Last login: Thu Dec  3 09:40:17 on ttys003
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cd ~/Downloads           [1]
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads]% ls             [2]
(mt) Mail.mobileconfig
11939352_895079043900778_767343162_o.jpg
30fab388b058befd15a085beabf47590.torrent
AdobeReader_dc_en_a_install.dmg
AnimataOSCExamples/
DataStructure2-Univers-2.pv
DataStructure2-Univers.pv
Deconstructed_Raincoat/
zsh_testfiles.tar
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads]% tar -xzf zsh_testfiles.tar  
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads]% cd Testfiles   [4]
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% l    [5]
total 152
-rw-r--r--@ 1 Kimberleyterheerdt  staff    17B Nov 26 10:24 april.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    18B Nov 26 10:25 august.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    21B Nov 26 10:26 december.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    20B Nov 26 10:24 february.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff     7B Nov 26 08:58 friday.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    30B Nov 26 10:23 january.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    16B Nov 26 10:25 july.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    16B Nov 26 10:25 june.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    17B Nov 26 10:24 march.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    15B Nov 26 10:25 may.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff     7B Nov 26 08:57 monday.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    21B Nov 26 10:26 november.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    20B Nov 26 10:26 october.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff     9B Nov 26 08:58 saturday.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    21B Nov 26 10:26 september.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff     7B Nov 26 08:58 sunday.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff     9B Nov 26 08:58 thursday.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff     8B Nov 26 08:57 tuesday.txt
-rw-r--r--@ 1 Kimberleyterheerdt  staff    10B Nov 26 08:57 wednesday.txt
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% mkdir Days
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% ls   [7]
Days/          february.txt   june.txt       november.txt   sunday.txt
april.txt      friday.txt     march.txt      october.txt    thursday.txt
august.txt     january.txt    may.txt        saturday.txt   tuesday.txt
december.txt   july.txt       monday.txt     september.txt  wednesday.txt
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% mv *day.txt /Days
usage: mv [-f | -i | -n] [-v] source target
       mv [-f | -i | -n] [-v] source ... directory
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% mkdir Months
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% mv *.txt /Months
usage: mv [-f | -i | -n] [-v] source target
       mv [-f | -i | -n] [-v] source ... directory
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% ls  [11]
Days/          february.txt   march.txt      saturday.txt   wednesday.txt
Months/        friday.txt     may.txt        september.txt
april.txt      january.txt    monday.txt     sunday.txt
august.txt     july.txt       november.txt   thursday.txt
december.txt   june.txt       october.txt    tuesday.txt
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% mv *days.txt
usage: mv [-f | -i | -n] [-v] source target
       mv [-f | -i | -n] [-v] source ... directory
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% ls  [13]
Days/          february.txt   march.txt      saturday.txt   wednesday.txt
Months/        friday.txt     may.txt        september.txt
april.txt      january.txt    monday.txt     sunday.txt
august.txt     july.txt       november.txt   thursday.txt
december.txt   june.txt       october.txt    tuesday.txt
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% mv *day.txt Days/
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% ls  [15]
Days/          august.txt     january.txt    march.txt      october.txt
Months/        december.txt   july.txt       may.txt        september.txt
april.txt      february.txt   june.txt       november.txt
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% mv *.txt Months/
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% ls  [17]
Days/   Months/
```