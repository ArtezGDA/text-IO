# Kimberley's work for Text IO 

## Homework
###1
[TheArray - Courses]() (python code)<br>
[TheDictionary - MyRoom]() (python code)<br>
[Data Dictionary - Itunes]() (python code)<br>
[Group Assignments - Fonts]() (python code)<br>

###2

[Days/Months]() (python code)<br>
[Days/Months - Ember]() (python code)<br>
[Cowsay]() (python code)<br>
[Edgar Allan Poe]() (python code)<br>
[Adobe Phone Home Behaviour]() (python code)<br>
<br>

###The Array

[The Array.pv](TheArray/TheArray.pv) <br>
 
```
courses = [['Photography', 'Design Philosophy'], ['Media Theory Annie', 'Design Research'], ['Digital Media', 'Computer Skills'], ['Graphic Design', 'Typography']]
print courses
print len (courses)
courses.insert(2,["Media Theory"])
print courses

print "Monthlyschedule"
for classes in courses: 
    
print "Monday", courses[0]
    print "Tuesday", courses[1]
    print "Wednesday", courses[2]
    print "Thursday", courses[3]
    print "friday", courses[4]
    
print "Month over!"

```
**TheArrayExtra.md**

```
courses = ['Photography', 'Design Philosophy', 'Media Theory Annie', 'Design Research', 'Digital Media', 'Computer Skills', 'Graphic Design', 'Typography']
print courses[0][1] #eerste woord tweede letter
print courses [0:1] #eerste woord met haakjes
print courses
courses[2]='les' # veranderd 2 (media theory) in les
print courses

```
**TheArrayTryOut.md**

```
courses = ['Photography', 'Design Philosophy', 'Media Theory Annie', 'Design Research', 'Digital Media', 'Computer Skills', 'Graphic Design', 'Typography']
print courses[0][1] #eerste woord tweede letter
print courses [0:1] #eerste woord met haakjes
print courses
courses[2]='les' # veranderd 2 (media theory) in les
print courses

```
###The Dictionary

[data_kth.py](TheDictionary/data_kth.py)

```
dict = {
"name":"Kimberley ter Heerdt",
"adress":"Sluiswachtershoeve",
"number":104,
"city":"Apeldoorn",
"postcode":7326, 
"roomsize":2, 
"ceilingheight":3,
"windows":1,
"doors":1,
"roomates":0,


```
[format_kth.py](TheDictionary/format_kth.py)

```
import data_kth

d = data_kth.dict

print "The Adress of %s's room is in %s, %s %d, %s. " % (d['name'],d['city'],d['adress'],d['number'],d['postcode'],)
print "My room is approximately %d big and the ceiling is %d high. " % (d['roomsize'],d['ceilingheight'])
print "On top of that I have %d window, and %d door" % (d['windows'],d['doors'], )


```
[format_friend.pv](TheDictionary/format_friend.pv)

```
import data_kth

d = data_kth.dict

print "The Adress of %s's room is in %s, %s %d, %s. " % (d['name'],d['city'],d['adress'],d['number'],d['postcode'],)
print "My room is approximately %d big and the ceiling is %d high. " % (d['roomsize'],d['ceilingheight'])
print "On top of that I have %d window, and %d door" % (d['windows'],d['doors'], )


import data_shirin

d = data_shirin.my_dict

print "In Comparison to my friends %s's room that is in %s, %s %d. " % (d['name'],d['city'],d['adress'],d['number'],)
print "Her room is approximately %d big and the ceiling is also %d high. " % (d['roomsize'],d['ceilingheight'])
print "She has %d windows, and also %d door." % (d['windows'],d['doors'], )


```
###Data Structure

[ItunesDictionary.pv](DataDictionaryI/ItunesDictionary.pv)

```

iTunes = {
    'Artist': 'Chilly Gonzales',
    'Biography': [{
          "Born": "March 20, 1972",
          "Genre": "Pop",
          "Years Active":"90's,'00s, '10s",
    }],
    'Albums' :  [
            {
                "name": "Solo Piano II ",
                "Released": "2014",
                "price":"$9.99",
                "Genre":["Pop", "Music", "Easy Listening", "Rock", "New Age"],
                "tracks": [
                    { 
                        "number": "1",
                        "title": "White Keys",
                        "duration": "3:06",
                        "price":"1,29"
                    },
                    { 
                        "number": "2",
                        "title": "Kenaston",
                        "duration": "3:04",
                        "price": "1,29"
                    },
                    { 
                        "number": "3",
                        "title": "Minor Fantasy",
                        "duration": "3:25",
                        "price": "1,29"
                    },
                    { 
                        "number": "4",
                        "title": "Escher",
                        "duration": "2:40",
                        "price": "1,29"
                    },
                    { 
                        "number": "5",
                        "title": "Rideaux Lunaires",
                        "duration": "2:39",
                        "price": "1,29"
                    },
                    { 
                        "number": "6",
                        "title": "Nero's Nocturne",
                        "duration": "2:15",
                        "price": "1,29"
                    },
                    { 
                        "number": "7",
                        "title": "Venetian Blinds",
                        "duration": "2:44",
                        "price": "1,29"
                    },
                    { 
                        "number": "8",
                        "title": "Evolving Doors",
                        "duration": "2:26",
                        "price": "1,29"
                    },
                    { 
                        "number": "9",
                        "title": "Epigram in E",
                        "duration": "2:58",
                        "price": "1,29"
                    },
                    { 
                        "number": "10",
                        "title": "Othello",
                        "duration": "3:15",
                        "price": "1,29"
                    },
                    { 
                        "number": "11",
                        "title": "Train of Thought",
                        "duration": "2:25",
                        "price": "1,29"
                    },
                    { 
                        "number": "12",
                        "title": "Wintermezzo",
                        "duration": "2:54",
                        "price": "1,29"
                    },
                    { 
                        "number": "13",
                        "title": "La Bulle",
                        "duration": "2:50",
                        "price": "1,29"
                    },
                    { 
                        "number": "14",
                        "title": "Papa Gavotte",
                        "duration": "2:45",
                        "price": "1,29"
                    },
                    { 
                        "number": "15",
                        "title": "Tarantelle",
                        "duration": "3:02",
                        "price": "1,29"
                    },
                    { 
                        "number": "16",
                        "title": "Amnesiac",
                        "duration": "2:25",
                        "price": "1,29"
                    },
                    { 
                        "number": "17",
                        "title": "Uncle",
                        "duration": "3:29",
                        "price": "1,29"
                    },
                    { 
                        "number": "18",
                        "title": "Composing Solo Piano I",
                        "duration": "4:34",
                        "price": "1,29"
                    },
                    { 
                        "number": "19",
                        "title": "Composing Solo Piano II",
                        "duration": "4:56",
                        "price": "1,29"
                    },
                    { 
                        "number": "20",
                        "title": "Composing Solo Piano III",
                        "duration": "5:05",
                        "price": "1,29"
                    },
                    { 
                        "number": "21",
                        "title": "White Keys",
                        "duration": "2:20",
                        "price": "1,29"
                    },
                    { 
                        "number": "22",
                        "title": "Kenaston",
                        "duration": "2:21",
                        "price": "1,29"
                    },
                    { 
                        "number": "23",
                        "title": "Minor Fantasy",
                        "duration": "1:55",
                        "price": "1,29"
                    },
                    { 
                        "number": "24",
                        "title": "Escher Presented",
                        "duration": "2:03",
                        "price": "1,29"
                    }
                    ]
            },
            
            {
                "name": "Ivory Tower",
                "Released": "2012",
                "price":"$9.99",
                "Genres": ["Pop","Music", "Dance", "Electronic", "House","Soundtrack","Soundtrack","Rock"],
                "tracks": [
                        { 
                        "number": "1",
                        "title": "Knight Moves",
                        "duration": "5:11",
                        "price": "1,29"
                        },
                        { 
                        "number": "2",
                        "title": "I am Europe",
                        "duration": "4:42",
                        "price": "1,29"
                        },
                        { 
                        "number": "3",
                        "title": "Bittersuite",
                        "duration": "3:40",
                        "price": "1,29"
                        },
                        { 
                        "number": "4",
                        "title": "Smothered Mate",
                        "duration": "6:03",
                        "price": "1,29"
                        },
                        { 
                        "number": "5",
                        "title": "The Grudge",
                        "duration": "3:14",
                        "price": "1,29"
                        },
                        { 
                        "number": "6",
                        "title": "Rococo Chanel",
                        "duration": "3:01",
                        "price": "1,29"
                        },
                        { 
                        "number": "7",
                        "title": "Never Stop",
                        "duration": "4:43",
                        "price": "1,29"
                        },
                        { 
                        "number": "8",
                        "title": "Pixel Paxil",
                        "duration": "3:57",
                        "price": "1,29"
                        },
                        { 
                        "number": "9",
                        "title": "You can Dance",
                        "duration": "5:10",
                        "price": "1,29"
                        },
                        { 
                        "number": "10",
                        "title": "Crying",
                        "duration": "4:49",
                        "price": "1,29"
                        },
                        { 
                        "number": "11",
                        "title": "Final Fantasy",
                        "duration": "5:41",
                        "price": "1,29"
                        },
                        { 
                        "number": "12",
                        "title": "Siren Song",
                        "duration": "3:29",
                        "price": "1,29"
                        },
                        { 
                        "number": "13",
                        "title": "Never Stop",
                        "duration": "3:50",
                        "price": "1,29"
                        },
                        { 
                        "number": "14",
                        "title": "Baroque Obama",
                        "duration": "3:54",
                        "price": "1,29"
                        }
                        
                        ]

            }
            
            ]
        
        }
print iTunes["Artist"]
print iTunes["Albums"][0]
print "NEXT ALBUM"
print iTunes["Albums"][1]

```


###Data Structure/Group Assignment
<br>


##2
<br>
###Days/Months
[DaysMonths](DaysMonths/DaysMonths.md)

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
###Ember
[Ember](DaysMonths/Ember.md)

```
Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]% cat Months/*ember.txt
Month 12 is December
Month 11 is November
Month 9 is September
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Downloads/Testfiles]%     [19]

```
###Cowsay
[Cowsay](Cowsay/Cowsay.md)

```
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
==> This script will install:
/usr/local/bin/brew
/usr/local/Library/...
/usr/local/share/man/man1/brew.1

Press RETURN to continue or any other key to abort
==> /usr/bin/sudo /bin/mkdir /usr/local

WARNING: Improper use of the sudo command could lead to data loss
or the deletion of important system files. Please double-check your
typing when using sudo. Type "man sudo" for more information.

To proceed, enter your password, or type Ctrl-C to abort.

Password:
Sorry, try again.
Password:
==> /usr/bin/sudo /bin/chmod g+rwx /usr/local
==> /usr/bin/sudo /usr/sbin/chown Kimberleyterheerdt:admin /usr/local
==> /usr/bin/sudo /bin/mkdir /Library/Caches/Homebrew
==> /usr/bin/sudo /bin/chmod g+rwx /Library/Caches/Homebrew
==> /usr/bin/sudo /usr/sbin/chown Kimberleyterheerdt /Library/Caches/Homebrew
==> Downloading and installing Homebrew...
remote: Counting objects: 3859, done.
remote: Compressing objects: 100% (3705/3705), done.
remote: Total 3859 (delta 41), reused 650 (delta 19), pack-reused 0
Receiving objects: 100% (3859/3859), 3.34 MiB | 1.51 MiB/s, done.
Resolving deltas: 100% (41/41), done.
From https://github.com/Homebrew/homebrew
 * [new branch]      master     -> origin/master
HEAD is now at aeeee75 centralize the logic of handling `homebrew-` in Tap.fetch
==> Installation successful!
==> Next steps
Run `brew help` to get started
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% install brew            [28]
usage: install [-bCcpSsv] [-B suffix] [-f flags] [-g group] [-m mode]
               [-o owner] file1 file2
       install [-bCcpSsv] [-B suffix] [-f flags] [-g group] [-m mode]
               [-o owner] file1 ... fileN directory
       install -d [-v] [-g group] [-m mode] [-o owner] directory ...
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% brew install cowsay     [29]
==> Downloading https://homebrew.bintray.com/bottles/cowsay-3.03.yosemite.bottle
######################################################################### 100.0%
==> Pouring cowsay-3.03.yosemite.bottle.1.tar.gz
🍺  /usr/local/Cellar/cowsay/3.03: 53 files, 228K
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cowsay "Welcome ladies and gentlemen!"
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) a
y "Moo"dquote> y "Moo"
dquote> 
dquote> "Moo"
dquote> "        
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% fortune                 [31]
zsh: correct fortune to _fortune ? ([Y]es/[N]o/[E]dit/[A]bort) y
_arguments:comparguments:312: can only be called from completion function
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% brew install fortune    [32]
==> Downloading https://homebrew.bintray.com/bottles/fortune-9708.yosemite.bottl
fortune
######################################################################### 100.0%
==> Pouring fortune-9708.yosemite.bottle.1.tar.gz
🍺  /usr/local/Cellar/fortune/9708: 116 files, 3.6M
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% fortune                 [33]
zsh: correct fortune to _fortune ? ([Y]es/[N]o/[E]dit/[A]bort) y
_arguments:comparguments:312: can only be called from completion function
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]%                         [34]
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% fortune                 [34]
zsh: correct fortune to _fortune ? ([Y]es/[N]o/[E]dit/[A]bort) 
Last login: Thu Dec  3 10:29:54 on ttys007
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% fortune                 [46]
I'll turn over a new leaf.
		-- Miguel de Cervantes
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cowsay "hoi kimberley"   [47]
 ______________ 
< hoi kimberley >
 -------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cowsay -f stegosaurus "hoi kimberley"
 ______________ 
< hoi kimberley >
 -------------- 
\                             .       .
 \                           / `.   .' " 
  \                  .---.  <    > <    >  .---.
   \                 |    \  \ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \~~~\.'                    `./~~~/
       ---------   \__/                        \__/
      .'  O    \     /               /       \  " 
     (_____,    `._.'               |         }  \/~~~/
      `----.          /       }     |        /    \__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cowsay -l               [49]
Cow files in /usr/local/Cellar/cowsay/3.03/share/cows:
beavis.zen bong bud-frogs bunny cheese cower daemon default dragon
dragon-and-cow elephant elephant-in-snake eyes flaming-sheep ghostbusters
head-in hellokitty kiss kitty koala kosh luke-koala meow milk moofasa moose
mutilated ren satanic sheep skeleton small sodomized stegosaurus stimpy
supermilker surgery telebears three-eyes turkey turtle tux udder vader
vader-koala www
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cowsay "Welcome ladies and gentlemen!"
dquote> "
 _______________________________ 
< Welcome ladies and gentlemen  >
 ------------------------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]%                         [52]
```

###Allen Poe
[Poe](Poe/Poe1.md)

```
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% mkdir Poe              [141]
mkdir: Poe: File exists
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% open Poe               [142]
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cd~/Poe                [143]
zsh: command not found: cd~/Poe
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cd Poe                 [144]
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Poe]%  curl http://www.gutenberg.org/files/2147/2147-8.txt > vol1.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   151k      0  0:00:03  0:00:03 --:--:--  151k
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Poe]% curl http://www.gutenberg.org/files/2148/2148-8.txt > vol2.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  566k  100  566k    0     0   178k      0  0:00:03  0:00:03 --:--:--  178k
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Poe]% curl http://www.gutenberg.org/files/2149/2149-8.txt > vol3.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  582k  100  582k    0     0   149k      0  0:00:03  0:00:03 --:--:--  149k
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Poe]% curl http://www.gutenberg.org/files/2150/2150-8.txt > vol4.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  475k  100  475k    0     0   178k      0  0:00:02  0:00:02 --:--:--  178k
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Poe]% curl http://www.gutenberg.org/files/2151/2151-8.txt > vol5.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  463k  100  463k    0     0   158k      0  0:00:02  0:00:02 --:--:--  158k
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Poe]% ls                 [149]
vol1.txt  vol2.txt  vol3.txt  vol4.txt  vol5.txt
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Poe]% cat vol*txt |grep -ci 'cat'
581
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Poe]% cat vol*.txt | grep -ci 'dog'
91
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Poe]% cat vol*.txt | grep -n 'horror'
583:subtle ramifications of its roots. In raising images of horror, also,
585:some terrible _doubt _which is the secret of all horror. He leaves to
609:the unreal as sources of effect. They have not used dread and horror
1367:any adequate idea of the horror of my situation. I gasped convulsively
1392:nor horror-stricken. If I felt any emotion at all, it was a kind of
1437:die rapidly away, and thereunto succeeded horror, and dismay, and a
2333:can give any adequate idea of the extreme, the absolute horror and
5003:every one present not less with horror than with astonishment.
5327:horror of the thing. But dismiss the idle opinions of this print. It
5665:brutal, a butchery without motive, a _grotesquerie_ in horror absolutely
5720:to all. I understood the full horrors of the murder at once.
5934:fell from his hold through excess of horror. Now it was that those
5959:horror, was just discernible. The fury of the beast, who no doubt bore
5974:Frenchman's exclamations of horror and affright, commingled with the
7596:in fact, a secret. The horrors of this dark deed are known only to one,
7693:unutterable horror at finding that the boat has been picked up and
8475:attended us. All around were horror, and thick gloom, and a black
8513:mainly inspired us with horror and astonishment, was that she bore up
8711:To conceive the horror of my sensations is, I presume, utterly
8728:horror upon horror! the ice opens suddenly to the right, and to the
10761:of the magnificence, or of the horror of the scene--or of the wild
10962:horror--for he put his mouth close to my ear, and screamed out the word
11019:the place at all. As it was, I involuntarily closed my eyes in horror.
11101:"Never shall I forget the sensations of awe, horror, and admiration with
11241:removed) speechless from the memory of its horror. Those who drew me on
12197:then present had been unaccustomed to death-bed horrors; but so hideous
12233:unutterable, shuddering horror which these few words, thus uttered, were
12399:the night's debauch--I experienced a sentiment half of horror, half of
12535:and horror with which the animal inspired me, had been heightened by one
12664:howl--a wailing shriek, half of horror and half of triumph, such as
12882:instruments, which did not inspire him with horror.
13131:horror, we partially turned aside the yet unscrewed lid of the coffin,
13181:intense sentiment of horror, unaccountable yet unendurable, I threw on
13510:redness and the horror of blood. There were sharp pains, and sudden
13650:surprise--then, finally, of terror, of horror, and of disgust.
13669:was besprinkled with the scarlet horror.
13714:horror at finding the grave-cerements and corpse-like mask which they
14167:horror become merged in a cloud of unnamable feeling. By gradations,
14174:delight of its horror. It is merely the idea of what would be our
14940:delirious horror, the soft and nearly imperceptible waving of the sable
14990:interminableness of the descent. They tell also of a vague horror at
15051:thronging upon my recollection a thousand vague rumors of the horrors of
15127:or death with its most hideous moral horrors. I had been reserved for
15191:my side on the floor. I saw, to my horror, that the pitcher had been
15192:removed. I say to my horror; for I was consumed with intolerable thirst.
15222:idea that had perceptibly descended. I now observed--with what horror it
15232:agents--the pit whose horrors had been destined for so bold a recusant
15242:What boots it to tell of the long, long hours of horror more than
15382:my wooden bed of horror upon the stone floor of the prison, when the
15414:A richer tint of crimson diffused itself over the pictured horrors of
15424:reason.--Oh! for a voice to speak!--oh! horror!--oh! any horror but
15625:no sooner was he awake than he became fully aware of the awful horrors
15708:which still palpitates, a degree of appalling and intolerable horror
15776:the grim Darkness overspread the Earth, then, with every horror of
15833:unstrung, and I fell a prey to perpetual horror. I hesitated to ride, or
17003:been already too much an object for the scorn--for the horror--for the
17030:am I not now dying a victim to the horror and the mystery of the wildest
17374:possessed with an objectless yet intolerable horror. Gasping for
17572:I say that I felt all the horrors of the damned? Most assuredly I had
17618:from Oxford to the continent, in a perfect agony of horror and of shame.
17717:astonishment, that horror which possessed me at the spectacle then
17924:horror!-this I thought, and this I think. But anything was better than
18184:dreams a cry as of horror and dismay; and thereunto, after a pause,
18200:comprehension. Yet its memory was replete with horror--horror more
18378:involved a penalty the exceeding great horror of which will not permit
19837:description. Every species of calamity and horror befell me. Among other
19988:My sensations were those of extreme horror and dismay. In vain I
20177:horror with which I was inspired by the fragmentary warning thus
20203:horrors which encompassed me. For another twenty-four hours it was
20544:What was his grief and horror in discovering that the latter had
21466:visitation, and that the appalling horror which has sometimes been
21469:anticipative horror, lest the apparition might possibly be real, than
21499:pitiable objects of horror and utter despair my eyes ever encountered.
21696:us more fully the horrors which surrounded us. The brig was a mere
21916:extremes first of delight and then of horror, than even any of the
21990:of her decks. Shall I ever forget the triple horror of that spectacle?
21998:raving with horror and despair--thoroughly mad through the anguish of
22174:indescribable state of weakness and horror, brought on by the wine,
22414:the tumultuous dangers of the storm or the gradually approaching horrors
22467:horror of their reality. Let it suffice to say that, having in some
22769:horror at the sound.
24426:horror not to be tolerated--never to be conceived.
24742:expressions of mingled horror, rage, and intense curiosity depicted
25004:all imagined horrors crowding upon me in fact. I felt my knees strike
25009:the cliff; and, with a wild, indefinable emotion, half of horror, half
25975:unutterable horror and awe, for which the language of mortality has no
25997:listened--in extremity of horror. The sound came again--it was a sigh.
26019:horrors of that night? Why shall I pause to relate how, time after
26112:horror, and the most beautiful became the most hideous, as Hinnon became
26202:gloom, and horror, and grief swept over it in clouds. I said the child
26234:and horror, for a worm that would not die.
26578:an unaccountable sentiment of horror has hitherto prevented me from
26598:altogether horrorless curiosity respecting yourself.
26987:I stood petrified with horror and rage. I endeavored to reply, but my
27743:the plunderer himself was often scared away by the horrors his own
27759:footsteps must have been palsied by the horrors of their situation. The
27878:manner, with a fit of what Tarpaulin called "the horrors." His jaws,
28088:with bottles of junk. The man with the horrors was drowned upon the
29544:box with a blindfold impetuosity--but who shall describe his horror when
29795:to the wall. To his extreme horror and astonishment, the head of the
29957:recoil in horror from the deep and impressive meaning of his terrible
30028:haste in the first place, and, in the second, a very usual horror at the
30730:emotions of wonder and horror with which I gazed, when, leaping
31350:my head gently to one side, I perceived, to my extreme horror, that the
31403:But now a new horror presented itself, and one indeed sufficient to
33732:insignificance, when to my extreme horror and astonishment I discovered
33949:the belligerents, and throwing open the sash to their extreme horror and
36464:terror, of horror, or of wo. You alone, habited in a white robe, passed
36766:general lamentation and horror. This first sense of pain lay in a
36787:details, of the fiery and horror-inspiring denunciations of the
36894:And then did we, the seven, start from our seats in horror, and stand
37877:on its breast, with a feeling or horror and awe--with a sentiment of
38322:shrieks of the multitude who gazed at them from below, horror-stricken,
38364:takes up a burthen so heavy in horror that it can be thrown down only
39139:seem to be rendered torpid, so that they have a horror of any thing like
39500:room fainted outright through sheer horror. But after the first wild,
41706:     And thy Angel I'll be, 'mid the horrors of this,--
42517:             What a horror they outpour
44188:  With horror and awe!
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~/Poe]%                    [153]
```
###Phone Behaviour
[Adobe Photoshop](Adobe Photoshop/AdobePhoneHomeBehaviour.md)


```
Last login: Thu Dec  3 10:01:49 on ttys004
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% netsat -a               [28]
zsh: correct netsat to netstat ? ([Y]es/[N]o/[E]dit/[A]bort) n
zsh: command not found: netsat
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% netstat -a              [29]
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)    
tcp4       0      0  192.168.217.104.59253  live.github.com.https  ESTABLISHED
tcp4       0      0  192.168.217.104.59204  live.github.com.https  ESTABLISHED
tcp4       0      0  192.168.217.104.59133  17.110.225.24.https    ESTABLISHED
tcp4       0      0  192.168.217.104.59010  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.59009  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.59000  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.58979  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.209.227.60364  n03.mail01.mtsvc.imaps ESTABLISHED
tcp4     143      0  192.168.209.227.59692  n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4     143      0  192.168.209.227.57313  n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4       0      0  *.7477                 *.*                    LISTEN     
tcp4       0      0  *.7476                 *.*                    LISTEN     
tcp4       0      0  *.7475                 *.*                    LISTEN     
tcp4       0      0  *.7474                 *.*                    LISTEN     
tcp4     143      0  192.168.0.24.59475     n03.mail01.mtsvc.imap  CLOSE_WAIT 
tcp4     143      0  192.168.0.24.62183     n03.mail01.mtsvc.imap  CLOSE_WAIT 
tcp4     143      0  192.168.0.24.59178     n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4       0      0  192.168.214.121.59145  n03.mail01.mtsvc.imaps ESTABLISHED
tcp4       0      0  localhost.ipp          *.*                    LISTEN     
tcp6       0      0  localhost.ipp          *.*                    LISTEN     
udp6       0      0  *.52477                *.*                               
udp4       0      0  *.52477                *.*                               
udp6       0      0  *.62204                *.*                               
udp4       0      0  *.62204                *.*                               
udp4       0      0  *.64857                *.*                               
udp6       0      0  *.61257                *.*                               
udp4       0      0  *.61257                *.*                               
udp6       0      0  *.60795                *.*                               
udp4       0      0  *.60795                *.*                               
udp4       0      0  192.168.217.104.ntp    *.*                               
udp6       0      0  macbook-pro-van-.ntp   *.*                               
udp6       0      0  macbook-pro-van-.ntp   *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
netudp6       0      0  fe80::1%lo0.ntp        *.*                               
udp4       0      0  localhost.ntp          *.*                               
udp6       0      0  localhost.ntp          *.*                               
udp6       0      0  *.ntp                  *.*                               
udp4       0      0  *.ntp                  *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.53257                *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp46      0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp6       0      0  *.mdns                 *.*                               
udp4       0      0  *.mdns                 *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.netbios-ns           *.*                               
udp4       0      0  *.netbios-dgm          *.*                               
Active Multipath Internet connections
Proto/ID  Flags      Local Address          Foreign Address        (state)    
icm6       0      0  *.*                    *.*                               
Active LOCAL (UNIX) domain sockets
Address          Type   Recv-Q Send-Q            Inode             Conn             Refs          Nextref Addr
70e74ebb63faaef9 stream      0      0                0 70e74ebb5deea531                0                0 /var/run/mDNSResponder
70e74ebb5deea531 stream      0      0                0 70e74ebb63faaef9                0                0
70e74ebb53c068b1 stream      0      0                0 70e74ebb68d82021                0                0 /var/run/mDNSResponder
70e74ebb68d82021 stream      0      0                0 70e74ebb53c068b1                0                0
70e74ebb63fa9789 stream      0      0                0 70e74ebb63fa9f59                0                0 /var/run/mDNSResponder
70e74ebb63fa9f59 stream      0      0                0 70e74ebb63fa9789                0                0
70e74ebb63fab089 stream      0      0                0 70e74ebb6178e219                0                0 /var/run/mDNSResponder
70e74ebb6178e219 stream      0      0                0 70e74ebb63fab089                0                0
70e74ebb5dccedc9 stream      0      0                0 70e74ebb5deea3a1                0                0 /var/run/mDNSResponder
70e74ebb5deea3a1 stream      0      0                0 70e74ebb5dccedc9                0                0
70e74ebb63faa8b9 stream      0      0                0 70e74ebb5dcd0089                0                0 /var/run/mDNSResponder
70e74ebb5dcd0089 stream      0      0                0 70e74ebb63faa8b9                0                0
70e74ebb58420fc1 stream      0      0                0                0                0                0
70e74ebb5dccdb09 stream      0      0                0 70e74ebb5dee97e9                0                0 /var/run/mDNSResponder
70e74ebb5dee97e9 stream      0      0                0 70e74ebb5dccdb09                0                0
70e74ebb68d82e31 stream      0      0                0                0                0                0
70e74ebb6178d599 stream      0      0                0 70e74ebb63faab11                0                0 /tmp/com.adobe.csi.ctrl-CS7-Kimberleyterheerdt
70e74ebb63faab11 stream      0      0                0 70e74ebb6178d599                0                0
70e74ebb5dee9e29 stream      0      0                0 70e74ebb53c06a41                0                0 /var/run/mDNSResponder
70e74ebb53c06a41 stream      0      0                0 70e74ebb5dee9e29                0                0
70e74ebb5dcce469 stream      0      0 70e74ebb562c5b31                0                0                0 /tmp/com.cycling74.501/mfl_706
70e74ebb6178dfc1 stream      0      0                0 70e74ebb5deebef9                0                0 /var/run/mDNSResponder
70e74ebb5deebef9 stream      0      0                0 70e74ebb6178dfc1                0                0
70e74ebb5dccf021 stream      0      0                0 70e74ebb68d80bd1                0                0 /var/run/mDNSResponder
70e74ebb68d80bd1 stream      0      0                0 70e74ebb5dccf021                0                0
70e74ebb5dccd8b1 stream      0      0 70e74ebb6786ba41                0                0                0 /var/folders/wq/d1dqs3g943s4hv8h_rjgrqy00000gn/T/ics8464
70e74ebb5dccf341 stream      0      0                0 70e74ebb5dccec39                0                0 /var/run/mDNSResponder
70e74ebb5dccec39 stream      0      0                0 70e74ebb5dccf341                0                0
70e74ebb5841f789 stream      0      0                0 70e74ebb5dcce919                0                0 /var/run/mDNSResponder
70e74ebb5dcce919 stream      0      0                0 70e74ebb5841f789                0                0
70e74ebb63fab3a9 stream      0      0                0 70e74ebb58421089                0                0 /var/run/mDNSResponder
70e74ebb58421089 stream      0      0                0 70e74ebb63fab3a9                0                0
70e74ebb5deeab71 stream      0      0                0 70e74ebb5dcce211                0                0 /var/run/mDNSResponder
70e74ebb5dcce211 stream      0      0                0 70e74ebb5deeab71                0                0
70e74ebb5deea789 stream      0      0                0 70e74ebb58420729                0                0 /var/run/mDNSResponder
70e74ebb58420729 stream      0      0                0 70e74ebb5deea789                0                0
70e74ebb58420d69 stream      0      0                0 70e74ebb63fab471                0                0 /var/run/mDNSResponder
70e74ebb63fab471 stream      0      0                0 70e74ebb58420d69                0                0
70e74ebb6178e089 stream      0      0                0 70e74ebb6178e471                0                0 /var/run/mDNSResponder
70e74ebb6178e471 stream      0      0                0 70e74ebb6178e089                0                0
70e74ebb5dccdbd1 stream      0      0 70e74ebb53b172b1                0                0                0 /tmp/com.adobe.csi.ctrl-CS7-Kimberleyterheerdt
70e74ebb5dccfef9 stream      0      0                0 70e74ebb5dcd0219                0                0 /var/run/mDNSResponder
70e74ebb5dcd0219 stream      0      0                0 70e74ebb5dccfef9                0                0
70e74ebb584200e9 stream      0      0                0 70e74ebb58420021                0                0 /var/run/mDNSResponder
70e74ebb58420021 stream      0      0                0 70e74ebb584200e9                0                0
70e74ebb58420661 stream      0      0                0 70e74ebb58420599                0                0 /var/run/usbmuxd
70e74ebb58420599 stream      0      0                0 70e74ebb58420661                0                0
70e74ebb53c06591 stream      0      0 70e74ebb581eca41                0                0                0 /var/folders/wq/d1dqs3g943s4hv8h_rjgrqy00000gn/T/icssuis501
70e74ebb53c06659 stream      0      0                0 70e74ebb53c06721                0                0
70e74ebb53c06721 stream      0      0                0 70e74ebb53c06659                0                0
70e74ebb53c06d61 stream      0      0                0 70e74ebb53c06ef1                0                0 /var/run/mDNSResponder
70e74ebb53c06ef1 stream      0      0                0 70e74ebb53c06d61                0                0
70e74ebb53c07081 stream      0      0                0 70e74ebb53c07149                0                0 /var/run/mDNSResponder
70e74ebb53c07149 stream      0      0                0 70e74ebb53c07081                0                0
70e74ebb53c07211 stream      0      0                0 70e74ebb53c072d9                0                0 /var/run/mDNSResponder
70e74ebb53c072d9 stream      0      0                0 70e74ebb53c07211                0                0
70e74ebb53c073a1 stream      0      0                0 70e74ebb53c07531                0                0 /var/run/mDNSResponder
70e74ebb53c07531 stream      0      0                0 70e74ebb53c073a1                0                0
70e74ebb53c07d01 stream      0      0 70e74ebb569382b1                0                0                0 /private/tmp/com.apple.launchd.CgP1Iqx5XM/Listeners
70e74ebb53c07c39 stream      0      0 70e74ebb56938491                0                0                0 /private/tmp/com.apple.launchd.Yf5A3lTtY5/Render
70e74ebb53c07469 stream      0      0 70e74ebb564d63a1                0                0                0 /var/tmp/filesystemui.socket
70e74ebb53c08279 stream      0      0                0 70e74ebb53c08341                0                0
70e74ebb53c08341 stream      0      0                0 70e74ebb53c08279                0                0
70e74ebb53c08661 stream      0      0 70e74ebb54c381c1                0                0                0 /var/run/pppconfd
70e74ebb53c088b9 stream      0      0 70e74ebb54119771                0                0                0 /private/var/run/cupsd
70e74ebb53c08981 stream      0      0 70e74ebb5411a0d1                0                0                0 /var/run/usbmuxd
70e74ebb53c08a49 stream      0      0 70e74ebb540c0951                0                0                0 /var/run/systemkeychaincheck.socket
70e74ebb53c08b11 stream      0      0 70e74ebb54098a41                0                0                0 /var/run/portmap.socket
70e74ebb53c08bd9 stream      0      0 70e74ebb54098fe1                0                0                0 /var/run/vpncontrol.sock
70e74ebb53c08ca1 stream      0      0 70e74ebb540690d1                0                0                0 /var/rpc/ncacn_np/srvsvc
70e74ebb53c08d69 stream      0      0 70e74ebb540691c1                0                0                0 /var/rpc/ncalrpc/srvsvc
70e74ebb53c08e31 stream      0      0 70e74ebb540692b1                0                0                0 /var/rpc/ncacn_np/wkssvc
70e74ebb53c08ef9 stream      0      0 70e74ebb540693a1                0                0                0 /var/rpc/ncalrpc/wkssvc
70e74ebb53c08fc1 stream      0      0 70e74ebb5405d681                0                0                0 /var/rpc/ncalrpc/NETLOGON
70e74ebb53c09089 stream      0      0 70e74ebb5405da41                0                0                0 /var/rpc/ncacn_np/mdssvc
70e74ebb53c09151 stream      0      0 70e74ebb5405db31                0                0                0 /var/rpc/ncacn_np/lsarpc
70e74ebb53c09219 stream      0      0 70e74ebb5405dd11                0                0                0 /var/rpc/ncalrpc/lsarpc
70e74ebb53c092e1 stream      0      0 70e74ebb5403ec21                0                0                0 /var/run/mDNSResponder
70e74ebb68d82661 dgram       0      0                0 70e74ebb68d82409 70e74ebb68d82409                0
70e74ebb68d82409 dgram       0      0                0 70e74ebb68d82661 70e74ebb68d82661                0
70e74ebb5dee9bd1 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb68d81d01
70e74ebb68d83151 dgram       0      0                0 70e74ebb5deeba49 70e74ebb5deeba49                0
70e74ebb5deeba49 dgram       0      0                0 70e74ebb68d83151 70e74ebb68d83151                0
70e74ebb68d81469 dgram       0      0                0 70e74ebb5deec089 70e74ebb5deec089                0
70e74ebb5deec089 dgram       0      0                0 70e74ebb68d81469 70e74ebb68d81469                0
70e74ebb68d81d01 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5deebb11
70e74ebb5deebb11 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5841f531
70e74ebb53c06bd1 dgram       0      0                0 70e74ebb5dcce9e1 70e74ebb5dcce9e1                0
70e74ebb5dcce9e1 dgram       0      0                0 70e74ebb53c06bd1 70e74ebb53c06bd1                0
70e74ebb5deea149 dgram       0      0                0 70e74ebb5841e591 70e74ebb5841e591                0
70e74ebb5841e591 dgram       0      0                0 70e74ebb5deea149 70e74ebb5deea149                0
70e74ebb5841f531 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb68d80721
70e74ebb68d833a9 dgram       0      0                0 70e74ebb5841f469 70e74ebb5841f469                0
70e74ebb5841f469 dgram       0      0                0 70e74ebb68d833a9 70e74ebb68d833a9                0
70e74ebb5dee9b09 dgram       0      0                0 70e74ebb5841f9e1 70e74ebb5841f9e1                0
70e74ebb5841f9e1 dgram       0      0                0 70e74ebb5dee9b09 70e74ebb5dee9b09                0
70e74ebb68d80721 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb584201b1
70e74ebb5dccf4d1 dgram       0      0                0 70e74ebb5dccf729 70e74ebb5dccf729                0
70e74ebb5dccf729 dgram       0      0                0 70e74ebb5dccf4d1 70e74ebb5dccf4d1                0
70e74ebb5deea211 dgram       0      0                0 70e74ebb5deea851 70e74ebb5deea851                0
70e74ebb5deea851 dgram       0      0                0 70e74ebb5deea211 70e74ebb5deea211                0
70e74ebb584201b1 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c06e29
70e74ebb53c06e29 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dee9d61
70e74ebb5841faa9 dgram       0      0                0 70e74ebb63faaa49 70e74ebb63faaa49                0
70e74ebb63faaa49 dgram       0      0                0 70e74ebb5841faa9 70e74ebb5841faa9                0
70e74ebb5dee98b1 dgram       0      0                0 70e74ebb5dcce5f9 70e74ebb5dcce5f9                0
70e74ebb5dcce5f9 dgram       0      0                0 70e74ebb5dee98b1 70e74ebb5dee98b1                0
70e74ebb63fa99e1 dgram       0      0                0 70e74ebb5deeae91 70e74ebb5deeae91                0
70e74ebb5deeae91 dgram       0      0                0 70e74ebb63fa99e1 70e74ebb63fa99e1                0
70e74ebb584212e1 dgram       0      0                0 70e74ebb58420279 70e74ebb58420279                0
70e74ebb58420279 dgram       0      0                0 70e74ebb584212e1 70e74ebb584212e1                0
70e74ebb68d82fc1 dgram       0      0                0 70e74ebb5deebe31 70e74ebb5deebe31                0
70e74ebb5deebe31 dgram       0      0                0 70e74ebb68d82fc1 70e74ebb68d82fc1                0
70e74ebb5deeb8b9 dgram       0      0                0 70e74ebb5841efb9 70e74ebb5841efb9                0
70e74ebb5841efb9 dgram       0      0                0 70e74ebb5deeb8b9 70e74ebb5deeb8b9                0
70e74ebb5dee9d61 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb6178d729
70e74ebb6178d729 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dcd0471
70e74ebb5dcd0471 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dcce851
70e74ebb5deeadc9 dgram       0      0                0 70e74ebb6178d8b9 70e74ebb6178d8b9                0
70e74ebb6178d8b9 dgram       0      0                0 70e74ebb5deeadc9 70e74ebb5deeadc9                0
70e74ebb63faa1b1 dgram       0      0                0 70e74ebb63faa279 70e74ebb63faa279                0
70e74ebb63faa279 dgram       0      0                0 70e74ebb63faa1b1 70e74ebb63faa1b1                0
70e74ebb63fa96c1 dgram       0      0                0 70e74ebb5deea6c1 70e74ebb5deea6c1                0
70e74ebb5deea6c1 dgram       0      0                0 70e74ebb63fa96c1 70e74ebb63fa96c1                0
70e74ebb5deead01 dgram       0      0                0 70e74ebb5dee9979 70e74ebb5dee9979                0
70e74ebb5dee9979 dgram       0      0                0 70e74ebb5deead01 70e74ebb5deead01                0
70e74ebb5dee9591 dgram       0      0                0 70e74ebb5dee9fb9 70e74ebb5dee9fb9                0
70e74ebb5dee9fb9 dgram       0      0                0 70e74ebb5dee9591 70e74ebb5dee9591                0
70e74ebb5dcce3a1 dgram       0      0                0 70e74ebb5dee9c99 70e74ebb5dee9c99                0
70e74ebb5dee9c99 dgram       0      0                0 70e74ebb5dcce3a1 70e74ebb5dcce3a1                0
70e74ebb5dccf981 dgram       0      0                0 70e74ebb5dccfbd9 70e74ebb5dccfbd9                0
70e74ebb5dccfbd9 dgram       0      0                0 70e74ebb5dccf981 70e74ebb5dccf981                0
70e74ebb5deebfc1 dgram       0      0                0 70e74ebb5841eb09 70e74ebb5841eb09                0
70e74ebb5841eb09 dgram       0      0                0 70e74ebb5deebfc1 70e74ebb5deebfc1                0
70e74ebb5841e721 dgram       0      0                0 70e74ebb5841ff59 70e74ebb5841ff59                0
70e74ebb5841ff59 dgram       0      0                0 70e74ebb5841e721 70e74ebb5841e721                0
70e74ebb5dcce851 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dccee91
70e74ebb5dccee91 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c067e9
70e74ebb5dccdc99 dgram       0      0                0 70e74ebb5841fc39 70e74ebb5841fc39                0
70e74ebb5841fc39 dgram       0      0                0 70e74ebb5dccdc99 70e74ebb5dccdc99                0
70e74ebb5841ec99 dgram       0      0                0 70e74ebb5841fd01 70e74ebb5841fd01                0
70e74ebb5841fd01 dgram       0      0                0 70e74ebb5841ec99 70e74ebb5841ec99                0
70e74ebb58420e31 dgram       0      0                0 70e74ebb5841eef1 70e74ebb5841eef1                0
70e74ebb5841eef1 dgram       0      0                0 70e74ebb58420e31 70e74ebb58420e31                0
70e74ebb53c07dc9 dgram       0      0                0 70e74ebb5841f3a1 70e74ebb5841f3a1                0
70e74ebb5841f3a1 dgram       0      0                0 70e74ebb53c07dc9 70e74ebb53c07dc9                0
70e74ebb5841f851 dgram       0      0                0 70e74ebb5841ebd1 70e74ebb5841ebd1                0
70e74ebb5841ebd1 dgram       0      0                0 70e74ebb5841f851 70e74ebb5841f851                0
70e74ebb58420b11 dgram       0      0                0 70e74ebb584208b9 70e74ebb584208b9                0
70e74ebb584208b9 dgram       0      0                0 70e74ebb58420b11 70e74ebb58420b11                0
70e74ebb53c067e9 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c06b09
70e74ebb53c06b09 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c08409
70e74ebb53c07f59 dgram       0      0                0 70e74ebb53c08021 70e74ebb53c08021                0
70e74ebb53c08021 dgram       0      0                0 70e74ebb53c07f59 70e74ebb53c07f59                0
70e74ebb53c075f9 dgram       0      0                0 70e74ebb53c076c1 70e74ebb53c076c1                0
70e74ebb53c076c1 dgram       0      0                0 70e74ebb53c075f9 70e74ebb53c075f9                0
70e74ebb53c07919 dgram       0      0                0 70e74ebb53c079e1 70e74ebb53c079e1                0
70e74ebb53c079e1 dgram       0      0                0 70e74ebb53c07919 70e74ebb53c07919                0
70e74ebb53c07aa9 dgram       0      0                0 70e74ebb53c07b71 70e74ebb53c07b71                0
70e74ebb53c07b71 dgram       0      0                0 70e74ebb53c07aa9 70e74ebb53c07aa9                0
70e74ebb53c080e9 dgram       0      0                0 70e74ebb53c081b1 70e74ebb53c081b1                0
70e74ebb53c081b1 dgram       0      0                0 70e74ebb53c080e9 70e74ebb53c080e9                0
70e74ebb53c08409 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c093a9
70e74ebb53c084d1 dgram       0      0                0 70e74ebb53c08599 70e74ebb53c08599                0
70e74ebb53c08599 dgram       0      0                0 70e74ebb53c084d1 70e74ebb53c084d1                0
70e74ebb53c08729 dgram       0      0                0 70e74ebb53c087f1 70e74ebb53c087f1                0
70e74ebb53c087f1 dgram       0      0                0 70e74ebb53c08729 70e74ebb53c08729                0
70e74ebb53c093a9 dgram       0      0                0 70e74ebb53c09471                0                0
70e74ebb53c09471 dgram       0      0 70e74ebb53c01fe1                0 70e74ebb5dee9bd1                0 /private//var/run/syslog
Registered kernel control modules
id       flags    pcbcount rcvbuf   sndbuf   name 
       1        9        0   131072     8192 com.apple.flow-divert 
       2        1        0    16384     2048 com.apple.nke.sockwall 
       3        9        0   524288   524288 com.apple.content-filter 
       4        9        0     8192     2048 com.apple.packet-mangler 
       5        1        1    65536    65536 com.apple.net.necp_control 
       6        9        0   524288   524288 com.apple.net.utun_control 
       7        1        0    65536    65536 com.apple.net.ipsec_control 
       8        0       18     8192     2048 com.apple.netsrc 
       9       18        0     8192     2048 com.apple.network.statistics 
       a        5        0     8192     2048 com.apple.network.tcp_ccdebug 
Active kernel event sockets
Proto Recv-Q Send-Q vendor  class subcla
kevt       0      0      1      6      1
kevt       0      0      1      1      2
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      1      1
kevt       0      0      1      1      2
kevt       0      0      1      1      2
kevt       0      0      1      6      1
kevt       0      0      1      1      0
Active kernel control sockets
Proto Recv-Q Send-Q   unit     id name
kctl       0      0      1      5 com.apple.net.necp_control
kctl       0      0      1      8 com.apple.netsrc
kctl       0      0      2      8 com.apple.netsrc
kctl       0      0      3      8 com.apple.netsrc
kctl       0      0      4      8 com.apple.netsrc
kctl       0      0      5      8 com.apple.netsrc
kctl       0      0      6      8 com.apple.netsrc
kctl       0      0      7      8 com.apple.netsrc
kctl       0      0      8      8 com.apple.netsrc
kctl       0      0      9      8 com.apple.netsrc
kctl       0      0     10      8 com.apple.netsrc
kctl       0      0     12      8 com.apple.netsrc
kctl       0      0     16      8 com.apple.netsrc
kctl       0      0     18      8 com.apple.netsrc
kctl       0      0     21      8 com.apple.netsrc
kctl       0      0     24      8 com.apple.netsrc
kctl       0      0     25      8 com.apple.netsrc
kctl       0      0     26      8 com.apple.netsrc
kctl       0      0     29      8 com.apple.netsrc
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% netstat -a grep 'adobe'
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)    
tcp4       0      0  192.168.217.104.59253  live.github.com.https  ESTABLISHED
tcp4       0      0  192.168.217.104.59204  live.github.com.https  ESTABLISHED
tcp4       0      0  192.168.217.104.59133  17.110.225.24.https    ESTABLISHED
tcp4       0      0  192.168.217.104.59010  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.59009  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.59000  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.58979  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.209.227.60364  n03.mail01.mtsvc.imaps ESTABLISHED
tcp4     143      0  192.168.209.227.59692  n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4     143      0  192.168.209.227.57313  n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4       0      0  *.7477                 *.*                    LISTEN     
tcp4       0      0  *.7476                 *.*                    LISTEN     
tcp4       0      0  *.7475                 *.*                    LISTEN     
tcp4       0      0  *.7474                 *.*                    LISTEN     
tcp4     143      0  192.168.0.24.59475     n03.mail01.mtsvc.imap  CLOSE_WAIT 
tcp4     143      0  192.168.0.24.62183     n03.mail01.mtsvc.imap  CLOSE_WAIT 
tcp4     143      0  192.168.0.24.59178     n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4       0      0  192.168.214.121.59145  n03.mail01.mtsvc.imaps ESTABLISHED
tcp4       0      0  localhost.ipp          *.*                    LISTEN     
tcp6       0      0  localhost.ipp          *.*                    LISTEN     
udp6       0      0  *.52477                *.*                               
udp4       0      0  *.52477                *.*                               
udp6       0      0  *.62204                *.*                               
udp4       0      0  *.62204                *.*                               
udp4       0      0  *.64857                *.*                               
udp6       0      0  *.61257                *.*                               
udp4       0      0  *.61257                *.*                               
udp6       0      0  *.60795                *.*                               
udp4       0      0  *.60795                *.*                               
udp4       0      0  192.168.217.104.ntp    *.*                               
udp6       0      0  macbook-pro-van-.ntp   *.*                               
udp6       0      0  macbook-pro-van-.ntp   *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp6       0      0  fe80::1%lo0.ntp        *.*                               
udp4       0      0  localhost.ntp          *.*                               
udp6       0      0  localhost.ntp          *.*                               
udp6       0      0  *.ntp                  *.*                               
udp4       0      0  *.ntp                  *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.53257                *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp46      0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp6       0      0  *.mdns                 *.*                               
udp4       0      0  *.mdns                 *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.netbios-ns           *.*                               
udp4       0      0  *.netbios-dgm          *.*                               
Active Multipath Internet connections
Proto/ID  Flags      Local Address          Foreign Address        (state)    
icm6       0      0  *.*                    *.*                               
Active LOCAL (UNIX) domain sockets
Address          Type   Recv-Q Send-Q            Inode             Conn             Refs          Nextref Addr
70e74ebb5deea531 stream      0      0                0 70e74ebb63faaef9                0                0 /var/run/mDNSResponder
70e74ebb63faaef9 stream      0      0                0 70e74ebb5deea531                0                0
70e74ebb53c068b1 stream      0      0                0 70e74ebb68d82021                0                0 /var/run/mDNSResponder
70e74ebb68d82021 stream      0      0                0 70e74ebb53c068b1                0                0
70e74ebb63fa9789 stream      0      0                0 70e74ebb63fa9f59                0                0 /var/run/mDNSResponder
70e74ebb63fa9f59 stream      0      0                0 70e74ebb63fa9789                0                0
70e74ebb63fab089 stream      0      0                0 70e74ebb6178e219                0                0 /var/run/mDNSResponder
70e74ebb6178e219 stream      0      0                0 70e74ebb63fab089                0                0
70e74ebb5dccedc9 stream      0      0                0 70e74ebb5deea3a1                0                0 /var/run/mDNSResponder
70e74ebb5deea3a1 stream      0      0                0 70e74ebb5dccedc9                0                0
70e74ebb63faa8b9 stream      0      0                0 70e74ebb5dcd0089                0                0 /var/run/mDNSResponder
70e74ebb5dcd0089 stream      0      0                0 70e74ebb63faa8b9                0                0
70e74ebb58420fc1 stream      0      0                0                0                0                0
70e74ebb5dccdb09 stream      0      0                0 70e74ebb5dee97e9                0                0 /var/run/mDNSResponder
70e74ebb5dee97e9 stream      0      0                0 70e74ebb5dccdb09                0                0
70e74ebb68d82e31 stream      0      0                0                0                0                0
70e74ebb6178d599 stream      0      0                0 70e74ebb63faab11                0                0 /tmp/com.adobe.csi.ctrl-CS7-Kimberleyterheerdt
70e74ebb63faab11 stream      0      0                0 70e74ebb6178d599                0                0
70e74ebb5dee9e29 stream      0      0                0 70e74ebb53c06a41                0                0 /var/run/mDNSResponder
70e74ebb53c06a41 stream      0      0                0 70e74ebb5dee9e29                0                0
70e74ebb5dcce469 stream      0      0 70e74ebb562c5b31                0                0                0 /tmp/com.cycling74.501/mfl_706
70e74ebb6178dfc1 stream      0      0                0 70e74ebb5deebef9                0                0 /var/run/mDNSResponder
70e74ebb5deebef9 stream      0      0                0 70e74ebb6178dfc1                0                0
70e74ebb5dccf021 stream      0      0                0 70e74ebb68d80bd1                0                0 /var/run/mDNSResponder
70e74ebb68d80bd1 stream      0      0                0 70e74ebb5dccf021                0                0
70e74ebb5dccd8b1 stream      0      0 70e74ebb6786ba41                0                0                0 /var/folders/wq/d1dqs3g943s4hv8h_rjgrqy00000gn/T/ics8464
70e74ebb5dccf341 stream      0      0                0 70e74ebb5dccec39                0                0 /var/run/mDNSResponder
70e74ebb5dccec39 stream      0      0                0 70e74ebb5dccf341                0                0
70e74ebb5841f789 stream      0      0                0 70e74ebb5dcce919                0                0 /var/run/mDNSResponder
70e74ebb5dcce919 stream      0      0                0 70e74ebb5841f789                0                0
70e74ebb63fab3a9 stream      0      0                0 70e74ebb58421089                0                0 /var/run/mDNSResponder
70e74ebb58421089 stream      0      0                0 70e74ebb63fab3a9                0                0
70e74ebb5deeab71 stream      0      0                0 70e74ebb5dcce211                0                0 /var/run/mDNSResponder
70e74ebb5dcce211 stream      0      0                0 70e74ebb5deeab71                0                0
70e74ebb5deea789 stream      0      0                0 70e74ebb58420729                0                0 /var/run/mDNSResponder
70e74ebb58420729 stream      0      0                0 70e74ebb5deea789                0                0
70e74ebb58420d69 stream      0      0                0 70e74ebb63fab471                0                0 /var/run/mDNSResponder
70e74ebb63fab471 stream      0      0                0 70e74ebb58420d69                0                0
70e74ebb6178e089 stream      0      0                0 70e74ebb6178e471                0                0 /var/run/mDNSResponder
70e74ebb6178e471 stream      0      0                0 70e74ebb6178e089                0                0
70e74ebb5dccdbd1 stream      0      0 70e74ebb53b172b1                0                0                0 /tmp/com.adobe.csi.ctrl-CS7-Kimberleyterheerdt
70e74ebb5dccfef9 stream      0      0                0 70e74ebb5dcd0219                0                0 /var/run/mDNSResponder
70e74ebb5dcd0219 stream      0      0                0 70e74ebb5dccfef9                0                0
70e74ebb584200e9 stream      0      0                0 70e74ebb58420021                0                0 /var/run/mDNSResponder
70e74ebb58420021 stream      0      0                0 70e74ebb584200e9                0                0
70e74ebb58420661 stream      0      0                0 70e74ebb58420599                0                0 /var/run/usbmuxd
70e74ebb58420599 stream      0      0                0 70e74ebb58420661                0                0
70e74ebb53c06591 stream      0      0 70e74ebb581eca41                0                0                0 /var/folders/wq/d1dqs3g943s4hv8h_rjgrqy00000gn/T/icssuis501
70e74ebb53c06659 stream      0      0                0 70e74ebb53c06721                0                0
70e74ebb53c06721 stream      0      0                0 70e74ebb53c06659                0                0
70e74ebb53c06d61 stream      0      0                0 70e74ebb53c06ef1                0                0 /var/run/mDNSResponder
70e74ebb53c06ef1 stream      0      0                0 70e74ebb53c06d61                0                0
70e74ebb53c07081 stream      0      0                0 70e74ebb53c07149                0                0 /var/run/mDNSResponder
70e74ebb53c07149 stream      0      0                0 70e74ebb53c07081                0                0
70e74ebb53c07211 stream      0      0                0 70e74ebb53c072d9                0                0 /var/run/mDNSResponder
70e74ebb53c072d9 stream      0      0                0 70e74ebb53c07211                0                0
70e74ebb53c073a1 stream      0      0                0 70e74ebb53c07531                0                0 /var/run/mDNSResponder
70e74ebb53c07531 stream      0      0                0 70e74ebb53c073a1                0                0
70e74ebb53c07d01 stream      0      0 70e74ebb569382b1                0                0                0 /private/tmp/com.apple.launchd.CgP1Iqx5XM/Listeners
70e74ebb53c07c39 stream      0      0 70e74ebb56938491                0                0                0 /private/tmp/com.apple.launchd.Yf5A3lTtY5/Render
70e74ebb53c07469 stream      0      0 70e74ebb564d63a1                0                0                0 /var/tmp/filesystemui.socket
70e74ebb53c08279 stream      0      0                0 70e74ebb53c08341                0                0
70e74ebb53c08341 stream      0      0                0 70e74ebb53c08279                0                0
70e74ebb53c08661 stream      0      0 70e74ebb54c381c1                0                0                0 /var/run/pppconfd
70e74ebb53c088b9 stream      0      0 70e74ebb54119771                0                0                0 /private/var/run/cupsd
70e74ebb53c08981 stream      0      0 70e74ebb5411a0d1                0                0                0 /var/run/usbmuxd
70e74ebb53c08a49 stream      0      0 70e74ebb540c0951                0                0                0 /var/run/systemkeychaincheck.socket
70e74ebb53c08b11 stream      0      0 70e74ebb54098a41                0                0                0 /var/run/portmap.socket
70e74ebb53c08bd9 stream      0      0 70e74ebb54098fe1                0                0                0 /var/run/vpncontrol.sock
70e74ebb53c08ca1 stream      0      0 70e74ebb540690d1                0                0                0 /var/rpc/ncacn_np/srvsvc
70e74ebb53c08d69 stream      0      0 70e74ebb540691c1                0                0                0 /var/rpc/ncalrpc/srvsvc
70e74ebb53c08e31 stream      0      0 70e74ebb540692b1                0                0                0 /var/rpc/ncacn_np/wkssvc
70e74ebb53c08ef9 stream      0      0 70e74ebb540693a1                0                0                0 /var/rpc/ncalrpc/wkssvc
70e74ebb53c08fc1 stream      0      0 70e74ebb5405d681                0                0                0 /var/rpc/ncalrpc/NETLOGON
70e74ebb53c09089 stream      0      0 70e74ebb5405da41                0                0                0 /var/rpc/ncacn_np/mdssvc
70e74ebb53c09151 stream      0      0 70e74ebb5405db31                0                0                0 /var/rpc/ncacn_np/lsarpc
70e74ebb53c09219 stream      0      0 70e74ebb5405dd11                0                0                0 /var/rpc/ncalrpc/lsarpc
70e74ebb53c092e1 stream      0      0 70e74ebb5403ec21                0                0                0 /var/run/mDNSResponder
70e74ebb68d82661 dgram       0      0                0 70e74ebb68d82409 70e74ebb68d82409                0
70e74ebb68d82409 dgram       0      0                0 70e74ebb68d82661 70e74ebb68d82661                0
70e74ebb5dee9bd1 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb68d81d01
70e74ebb68d83151 dgram       0      0                0 70e74ebb5deeba49 70e74ebb5deeba49                0
70e74ebb5deeba49 dgram       0      0                0 70e74ebb68d83151 70e74ebb68d83151                0
70e74ebb68d81469 dgram       0      0                0 70e74ebb5deec089 70e74ebb5deec089                0
70e74ebb5deec089 dgram       0      0                0 70e74ebb68d81469 70e74ebb68d81469                0
70e74ebb68d81d01 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5deebb11
70e74ebb5deebb11 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5841f531
70e74ebb53c06bd1 dgram       0      0                0 70e74ebb5dcce9e1 70e74ebb5dcce9e1                0
70e74ebb5dcce9e1 dgram       0      0                0 70e74ebb53c06bd1 70e74ebb53c06bd1                0
70e74ebb5deea149 dgram       0      0                0 70e74ebb5841e591 70e74ebb5841e591                0
70e74ebb5841e591 dgram       0      0                0 70e74ebb5deea149 70e74ebb5deea149                0
70e74ebb5841f531 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb68d80721
70e74ebb68d833a9 dgram       0      0                0 70e74ebb5841f469 70e74ebb5841f469                0
70e74ebb5841f469 dgram       0      0                0 70e74ebb68d833a9 70e74ebb68d833a9                0
70e74ebb5dee9b09 dgram       0      0                0 70e74ebb5841f9e1 70e74ebb5841f9e1                0
70e74ebb5841f9e1 dgram       0      0                0 70e74ebb5dee9b09 70e74ebb5dee9b09                0
70e74ebb68d80721 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb584201b1
70e74ebb5dccf4d1 dgram       0      0                0 70e74ebb5dccf729 70e74ebb5dccf729                0
70e74ebb5dccf729 dgram       0      0                0 70e74ebb5dccf4d1 70e74ebb5dccf4d1                0
70e74ebb5deea211 dgram       0      0                0 70e74ebb5deea851 70e74ebb5deea851                0
70e74ebb5deea851 dgram       0      0                0 70e74ebb5deea211 70e74ebb5deea211                0
70e74ebb584201b1 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c06e29
70e74ebb53c06e29 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dee9d61
70e74ebb5841faa9 dgram       0      0                0 70e74ebb63faaa49 70e74ebb63faaa49                0
70e74ebb63faaa49 dgram       0      0                0 70e74ebb5841faa9 70e74ebb5841faa9                0
70e74ebb5dee98b1 dgram       0      0                0 70e74ebb5dcce5f9 70e74ebb5dcce5f9                0
70e74ebb5dcce5f9 dgram       0      0                0 70e74ebb5dee98b1 70e74ebb5dee98b1                0
70e74ebb63fa99e1 dgram       0      0                0 70e74ebb5deeae91 70e74ebb5deeae91                0
70e74ebb5deeae91 dgram       0      0                0 70e74ebb63fa99e1 70e74ebb63fa99e1                0
70e74ebb584212e1 dgram       0      0                0 70e74ebb58420279 70e74ebb58420279                0
70e74ebb58420279 dgram       0      0                0 70e74ebb584212e1 70e74ebb584212e1                0
70e74ebb68d82fc1 dgram       0      0                0 70e74ebb5deebe31 70e74ebb5deebe31                0
70e74ebb5deebe31 dgram       0      0                0 70e74ebb68d82fc1 70e74ebb68d82fc1                0
70e74ebb5deeb8b9 dgram       0      0                0 70e74ebb5841efb9 70e74ebb5841efb9                0
70e74ebb5841efb9 dgram       0      0                0 70e74ebb5deeb8b9 70e74ebb5deeb8b9                0
70e74ebb5dee9d61 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb6178d729
70e74ebb6178d729 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dcd0471
70e74ebb5dcd0471 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dcce851
70e74ebb5deeadc9 dgram       0      0                0 70e74ebb6178d8b9 70e74ebb6178d8b9                0
70e74ebb6178d8b9 dgram       0      0                0 70e74ebb5deeadc9 70e74ebb5deeadc9                0
70e74ebb63faa1b1 dgram       0      0                0 70e74ebb63faa279 70e74ebb63faa279                0
70e74ebb63faa279 dgram       0      0                0 70e74ebb63faa1b1 70e74ebb63faa1b1                0
70e74ebb63fa96c1 dgram       0      0                0 70e74ebb5deea6c1 70e74ebb5deea6c1                0
70e74ebb5deea6c1 dgram       0      0                0 70e74ebb63fa96c1 70e74ebb63fa96c1                0
70e74ebb5deead01 dgram       0      0                0 70e74ebb5dee9979 70e74ebb5dee9979                0
70e74ebb5dee9979 dgram       0      0                0 70e74ebb5deead01 70e74ebb5deead01                0
70e74ebb5dee9591 dgram       0      0                0 70e74ebb5dee9fb9 70e74ebb5dee9fb9                0
70e74ebb5dee9fb9 dgram       0      0                0 70e74ebb5dee9591 70e74ebb5dee9591                0
70e74ebb5dcce3a1 dgram       0      0                0 70e74ebb5dee9c99 70e74ebb5dee9c99                0
70e74ebb5dee9c99 dgram       0      0                0 70e74ebb5dcce3a1 70e74ebb5dcce3a1                0
70e74ebb5dccf981 dgram       0      0                0 70e74ebb5dccfbd9 70e74ebb5dccfbd9                0
70e74ebb5dccfbd9 dgram       0      0                0 70e74ebb5dccf981 70e74ebb5dccf981                0
70e74ebb5deebfc1 dgram       0      0                0 70e74ebb5841eb09 70e74ebb5841eb09                0
70e74ebb5841eb09 dgram       0      0                0 70e74ebb5deebfc1 70e74ebb5deebfc1                0
70e74ebb5841e721 dgram       0      0                0 70e74ebb5841ff59 70e74ebb5841ff59                0
70e74ebb5841ff59 dgram       0      0                0 70e74ebb5841e721 70e74ebb5841e721                0
70e74ebb5dcce851 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dccee91
70e74ebb5dccee91 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c067e9
70e74ebb5dccdc99 dgram       0      0                0 70e74ebb5841fc39 70e74ebb5841fc39                0
70e74ebb5841fc39 dgram       0      0                0 70e74ebb5dccdc99 70e74ebb5dccdc99                0
70e74ebb5841ec99 dgram       0      0                0 70e74ebb5841fd01 70e74ebb5841fd01                0
70e74ebb5841fd01 dgram       0      0                0 70e74ebb5841ec99 70e74ebb5841ec99                0
70e74ebb58420e31 dgram       0      0                0 70e74ebb5841eef1 70e74ebb5841eef1                0
70e74ebb5841eef1 dgram       0      0                0 70e74ebb58420e31 70e74ebb58420e31                0
70e74ebb53c07dc9 dgram       0      0                0 70e74ebb5841f3a1 70e74ebb5841f3a1                0
70e74ebb5841f3a1 dgram       0      0                0 70e74ebb53c07dc9 70e74ebb53c07dc9                0
70e74ebb5841f851 dgram       0      0                0 70e74ebb5841ebd1 70e74ebb5841ebd1                0
70e74ebb5841ebd1 dgram       0      0                0 70e74ebb5841f851 70e74ebb5841f851                0
70e74ebb58420b11 dgram       0      0                0 70e74ebb584208b9 70e74ebb584208b9                0
70e74ebb584208b9 dgram       0      0                0 70e74ebb58420b11 70e74ebb58420b11                0
70e74ebb53c067e9 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c06b09
70e74ebb53c06b09 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c08409
70e74ebb53c07f59 dgram       0      0                0 70e74ebb53c08021 70e74ebb53c08021                0
70e74ebb53c08021 dgram       0      0                0 70e74ebb53c07f59 70e74ebb53c07f59                0
70e74ebb53c075f9 dgram       0      0                0 70e74ebb53c076c1 70e74ebb53c076c1                0
70e74ebb53c076c1 dgram       0      0                0 70e74ebb53c075f9 70e74ebb53c075f9                0
70e74ebb53c07919 dgram       0      0                0 70e74ebb53c079e1 70e74ebb53c079e1                0
70e74ebb53c079e1 dgram       0      0                0 70e74ebb53c07919 70e74ebb53c07919                0
70e74ebb53c07aa9 dgram       0      0                0 70e74ebb53c07b71 70e74ebb53c07b71                0
70e74ebb53c07b71 dgram       0      0                0 70e74ebb53c07aa9 70e74ebb53c07aa9                0
70e74ebb53c080e9 dgram       0      0                0 70e74ebb53c081b1 70e74ebb53c081b1                0
70e74ebb53c081b1 dgram       0      0                0 70e74ebb53c080e9 70e74ebb53c080e9                0
70e74ebb53c08409 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c093a9
70e74ebb53c084d1 dgram       0      0                0 70e74ebb53c08599 70e74ebb53c08599                0
70e74ebb53c08599 dgram       0      0                0 70e74ebb53c084d1 70e74ebb53c084d1                0
70e74ebb53c08729 dgram       0      0                0 70e74ebb53c087f1 70e74ebb53c087f1                0
70e74ebb53c087f1 dgram       0      0                0 70e74ebb53c08729 70e74ebb53c08729                0
70e74ebb53c093a9 dgram       0      0                0 70e74ebb53c09471                0                0
70e74ebb53c09471 dgram       0      0 70e74ebb53c01fe1                0 70e74ebb5dee9bd1                0 /private//var/run/syslog
Registered kernel control modules
id       flags    pcbcount rcvbuf   sndbuf   name 
       1        9        0   131072     8192 com.apple.flow-divert 
       2        1        0    16384     2048 com.apple.nke.sockwall 
       3        9        0   524288   524288 com.apple.content-filter 
       4        9        0     8192     2048 com.apple.packet-mangler 
       5        1        1    65536    65536 com.apple.net.necp_control 
       6        9        0   524288   524288 com.apple.net.utun_control 
       7        1        0    65536    65536 com.apple.net.ipsec_control 
       8        0       18     8192     2048 com.apple.netsrc 
       9       18        0     8192     2048 com.apple.network.statistics 
       a        5        0     8192     2048 com.apple.network.tcp_ccdebug 
Active kernel event sockets
Proto Recv-Q Send-Q vendor  class subcla
kevt       0      0      1      6      1
kevt       0      0      1      1      2
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      1      1
kevt       0      0      1      1      2
kevt       0      0      1      1      2
kevt       0      0      1      6      1
kevt       0      0      1      1      0
Active kernel control sockets
Proto Recv-Q Send-Q   unit     id name
kctl       0      0      1      5 com.apple.net.necp_control
kctl       0      0      1      8 com.apple.netsrc
kctl       0      0      2      8 com.apple.netsrc
kctl       0      0      3      8 com.apple.netsrc
kctl       0      0      4      8 com.apple.netsrc
kctl       0      0      5      8 com.apple.netsrc
kctl       0      0      6      8 com.apple.netsrc
kctl       0      0      7      8 com.apple.netsrc
kctl       0      0      8      8 com.apple.netsrc
kctl       0      0      9      8 com.apple.netsrc
kctl       0      0     10      8 com.apple.netsrc
kctl       0      0     12      8 com.apple.netsrc
kctl       0      0     16      8 com.apple.netsrc
kctl       0      0     18      8 com.apple.netsrc
kctl       0      0     21      8 com.apple.netsrc
kctl       0      0     24      8 com.apple.netsrc
kctl       0      0     25      8 com.apple.netsrc
kctl       0      0     26      8 com.apple.netsrc
kctl       0      0     29      8 com.apple.netsrc
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]%                                                                                                   [31]
```

## Concept
he Concept is to make a program in the terminal.
This program will show you short motivational short messages hourly like: **"Good Job!"**,**"You can do this!"**,**"Awesome!"** and more. The program is dedicated to give people that ""little push in the back"". You can put these Motivational messages on (when you need them) and off (When you can handle it all by yourself) in your terminal. 

The text will be showed in the Notification Center, so you dont have to switch to the Terminal but it will show you


osascript -e 'display notification "Good Job!" with title "Motivation"'
osascript -e 'display notification "Awesome!" with title "Motivation"'
osascript -e 'display notification "You can do this!" with title "Motivation"'


## Prototype: working demo

## Design the flow of the program

## How to use the script

## PDF format 
			
