# Sietske's work for Text IO 

## Homework
[the Array](textIO/array-courses.pv)

```
**Array in Terminal**

>>> [0, 1, 2, 3]
[0, 1, 2, 3]
>>> reeks = [0, 1, 2, 3]
>>> reeks
[0, 1, 2, 3]
>>> naam = "Sietske"
>>> vakken = ["Media Design", "Photography", "Typography"]
>>> vakken
['Media Design', 'Photography', 'Typography']
>>> len(vakken)
3
>>> vakken.append("Graphic Design")
>>> len(vakken)
4
>>> vakken.pop()
'Graphic Design'
>>> len(vakken)
3
>>> print len(vakken)
3
>>> vakken = vakken + ["Graphic Design", "Philosophy"]
>>> len(vakken)
5
>>> vakken.pop()
'Philosophy'
>>> vakken.pop()
'Graphic Design'
>>> vakken.pop()
'Typography'
>>> vakken
['Media Design', 'Photography']
>>> vakken = vakken + ["Graphic Design", "Philosophy"]
>>> vakken
['Media Design', 'Photography', 'Graphic Design', 'Philosophy']
>>> del vakken[1]
>>> vakken
['Media Design', 'Graphic Design', 'Philosophy']
``` 

[Dictionary](textIO/dictionary-room.pv)

[Data structure I](textIO/data-structure1-albums01.pv),
[Data structure I](textIO/data-structure1-albums02.pv),
[Data structure I](textIO/data-structure1-albums03.pv),
[Data structure I](textIO/data-structure1-albums04.pv)

##Exercices for working with the shell

###1. Months and Days
```
[sietskebarten@TreeHouse: ~]% cd Documents                                 [65]
[sietskebarten@TreeHouse: ~/Documents]% cd Testfiles                       [66]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mkdir Days               [67]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mkdir Months             [68]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% ls                       [69]
Days/          february.txt   march.txt      october.txt    tuesday.txt
Months/        friday.txt     may.txt        saturday.txt   wednesday.txt
april.txt      january.txt    mobydick.txt   september.txt
august.txt     july.txt       monday.txt     sunday.txt
december.txt   june.txt       november.txt   thursday.txt
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv *day.txt Days/        [70]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% ls                       [71]
Days/          august.txt     january.txt    march.txt      november.txt
Months/        december.txt   july.txt       may.txt        october.txt
april.txt      february.txt   june.txt       mobydick.txt   september.txt
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv *month.txt Months/    [72]
mv: rename *month.txt to Months/*month.txt: No such file or directory
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv *month.txt Months     [73]
mv: rename *month.txt to Months/*month.txt: No such file or directory
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv *ember.txt Months     [74]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv *ary.txt Months       [75]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv *ber.txt Monts        [76]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv april.txt Months      [77]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv may.txt Months        [78]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv march.txt Months      [79]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv june.txt Months       [81]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv july.txt Months       [82]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv au[sietskebarten@TreeHouse: ~/
Documents/Testfiles]% mv october.txt Months    [86]
```
### 2. Search files
```
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% cat Months/*ember.txt    [87]
Month 12 is December
Month 11 is November
Month 9 is September
gus.txt Months      [83]
mv: rename augus.txt to Months/augus.txt: No such file or directory
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv august.txt Months     [84]

```
### 3. Cowsay
```
[sietskebarten@TreeHouse: ~]% cowsay "Moo"                                 [97]
 _____ 
< Moo >
 ----- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
[sietskebarten@TreeHouse: ~]% fortune                                      [98]
"I believe the use of noise to make music will increase until we reach a
music produced through the aid of electrical instruments which will make
available for musical purposes any and all sounds that can be heard."
-- composer John Cage, 1937

[sietskebarten@TreeHouse: ~]% cowsay -f stegosaurus "Welcome ladies and gentlemen!" 
 _______________________________ 
< Welcome ladies and gentlemen  >
 ------------------------------- 
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

```

###4. Research Edgar Allan Poe
```
[sietskebarten@TreeHouse: ~/Documents]% curl http://www.gutenberg.org/files/2147/2147-8.txt > vol1.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   468k      0  0:00:01  0:00:01 --:--:--  468k
[sietskebarten@TreeHouse: ~/Documents]% curl  http://www.gutenberg.org/files/2148/2148-8.txt > vol2.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  566k  100  566k    0     0   426k      0  0:00:01  0:00:01 --:--:--  426k
[sietskebarten@TreeHouse: ~/Documents]% curl http://www.gutenberg.org/files/2148/2148-8.txt >| vol3.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  566k  100  566k    0     0   361k      0  0:00:01  0:00:01 --:--:--  361k
[sietskebarten@TreeHouse: ~/Documents]% curl  http://www.gutenberg.org/files/2150/2150-8.txt > vol4.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  475k  100  475k    0     0   365k      0  0:00:01  0:00:01 --:--:--  365k
[sietskebarten@TreeHouse: ~/Documents]% curl  http://www.gutenberg.org/files/2149/2149-8.txt > vol3.txt
zsh: file exists: vol3.txt
[sietskebarten@TreeHouse: ~/Documents]% curl http://www.gutenberg.org/files/2149/2149-8.txt >| vol3.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  582k  100  582k    0     0   236k      0  0:00:02  0:00:02 --:--:--  236k
[sietskebarten@TreeHouse: ~/Documents]% curl  http://www.gutenberg.org/files/2151/2151-8.txt > vol5.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  463k  100  463k    0     0   337k      0  0:00:01  0:00:01 --:--:--  337k
[sietskebarten@TreeHouse: ~/Documents]% mv vol*.txt Poe                    [93]
usage: mv [-f | -i | -n] [-v] source target
       mv [-f | -i | -n] [-v] source ... directory
[sietskebarten@TreeHouse: ~/Documents]% mv vol*.txt Poe/                   [94]
usage: mv [-f | -i | -n] [-v] source target
       mv [-f | -i | -n] [-v] source ... directory
[sietskebarten@TreeHouse: ~/Documents]% mv vol1.txt Poe/                   [95]
mv: rename vol1.txt to Poe/: No such file or directory
[sietskebarten@TreeHouse: ~/Documents]% mv vol*.txt Testfiles              [96]
[sietskebarten@TreeHouse: ~/Documents]% mv vol*.txt Poe                    [97]
mv: rename vol*.txt to Poe: No such file or directory
[sietskebarten@TreeHouse: ~/Documents]% cd Testfiles                       [98]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% mv vol*.txt Poe          [99]
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% grep -ci  "cat" vol*.txt
egrep: vol*.txt: No such file or directory
[sietskebarten@TreeHouse: ~/Documents/Testfiles]% cd Poe                  [101]
[sietskebarten@TreeHouse: Documents/Testfiles/Poe]% grep -ci "cat" vol*.txt
vol1.txt:133
vol2.txt:138
vol3.txt:114
vol4.txt:116
vol5.txt:80
[sietskebarten@TreeHouse: Documents/Testfiles/Poe]% grep -ci "dog" vol*.txt
vol1.txt:10
vol2.txt:17
vol3.txt:23
vol4.txt:28
vol5.txt:13
[sietskebarten@TreeHouse: Documents/Testfiles/Poe]% grep -ci "horror" vol*.txt
vol1.txt:21
vol2.txt:48
vol3.txt:34
vol4.txt:14
vol5.txt:10
[sietskebarten@TreeHouse: Documents/Testfiles/Poe]% grep -ci "Is Poe a cat or a dog person?" vol*.txt
vol1.txt:0
vol2.txt:0
vol3.txt:0
vol4.txt:0
vol5.txt:0

```
## Concept

## Prototype: working demo

## Design the flow of the program

## How to use the script

## PDF format 
			
