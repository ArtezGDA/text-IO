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
[sietskebarten@TreeHouse: Documents/Testfiles/Poe]% grep -n "horror" vol*.txt
vol1.txt:583:subtle ramifications of its roots. In raising images of horror, also,
vol1.txt:585:some terrible _doubt _which is the secret of all horror. He leaves to
vol1.txt:609:the unreal as sources of effect. They have not used dread and horror
vol1.txt:1367:any adequate idea of the horror of my situation. I gasped convulsively
vol1.txt:1392:nor horror-stricken. If I felt any emotion at all, it was a kind of
vol1.txt:1437:die rapidly away, and thereunto succeeded horror, and dismay, and a
vol1.txt:2333:can give any adequate idea of the extreme, the absolute horror and
vol1.txt:5003:every one present not less with horror than with astonishment.
vol1.txt:5327:horror of the thing. But dismiss the idle opinions of this print. It
vol1.txt:5665:brutal, a butchery without motive, a _grotesquerie_ in horror absolutely
vol1.txt:5720:to all. I understood the full horrors of the murder at once.
vol1.txt:5934:fell from his hold through excess of horror. Now it was that those
vol1.txt:5959:horror, was just discernible. The fury of the beast, who no doubt bore
vol1.txt:5974:Frenchman's exclamations of horror and affright, commingled with the
vol1.txt:7596:in fact, a secret. The horrors of this dark deed are known only to one,
vol1.txt:7693:unutterable horror at finding that the boat has been picked up and
vol1.txt:8475:attended us. All around were horror, and thick gloom, and a black
vol1.txt:8513:mainly inspired us with horror and astonishment, was that she bore up
vol1.txt:8711:To conceive the horror of my sensations is, I presume, utterly
vol1.txt:8728:horror upon horror! the ice opens suddenly to the right, and to the
vol2.txt:1535:of the magnificence, or of the horror of the scene--or of the wild
vol2.txt:1736:horror--for he put his mouth close to my ear, and screamed out the word
vol2.txt:1793:the place at all. As it was, I involuntarily closed my eyes in horror.
vol2.txt:1875:"Never shall I forget the sensations of awe, horror, and admiration with
vol2.txt:2015:removed) speechless from the memory of its horror. Those who drew me on
vol2.txt:2971:then present had been unaccustomed to death-bed horrors; but so hideous
vol2.txt:3007:unutterable, shuddering horror which these few words, thus uttered, were
vol2.txt:3173:the night's debauch--I experienced a sentiment half of horror, half of
vol2.txt:3309:and horror with which the animal inspired me, had been heightened by one
vol2.txt:3438:howl--a wailing shriek, half of horror and half of triumph, such as
vol2.txt:3656:instruments, which did not inspire him with horror.
vol2.txt:3905:horror, we partially turned aside the yet unscrewed lid of the coffin,
vol2.txt:3955:intense sentiment of horror, unaccountable yet unendurable, I threw on
vol2.txt:4284:redness and the horror of blood. There were sharp pains, and sudden
vol2.txt:4424:surprise--then, finally, of terror, of horror, and of disgust.
vol2.txt:4443:was besprinkled with the scarlet horror.
vol2.txt:4488:horror at finding the grave-cerements and corpse-like mask which they
vol2.txt:4941:horror become merged in a cloud of unnamable feeling. By gradations,
vol2.txt:4948:delight of its horror. It is merely the idea of what would be our
vol2.txt:5714:delirious horror, the soft and nearly imperceptible waving of the sable
vol2.txt:5764:interminableness of the descent. They tell also of a vague horror at
vol2.txt:5825:thronging upon my recollection a thousand vague rumors of the horrors of
vol2.txt:5901:or death with its most hideous moral horrors. I had been reserved for
vol2.txt:5965:my side on the floor. I saw, to my horror, that the pitcher had been
vol2.txt:5966:removed. I say to my horror; for I was consumed with intolerable thirst.
vol2.txt:5996:idea that had perceptibly descended. I now observed--with what horror it
vol2.txt:6006:agents--the pit whose horrors had been destined for so bold a recusant
vol2.txt:6016:What boots it to tell of the long, long hours of horror more than
vol2.txt:6156:my wooden bed of horror upon the stone floor of the prison, when the
vol2.txt:6188:A richer tint of crimson diffused itself over the pictured horrors of
vol2.txt:6198:reason.--Oh! for a voice to speak!--oh! horror!--oh! any horror but
vol2.txt:6399:no sooner was he awake than he became fully aware of the awful horrors
vol2.txt:6482:which still palpitates, a degree of appalling and intolerable horror
vol2.txt:6550:the grim Darkness overspread the Earth, then, with every horror of
vol2.txt:6607:unstrung, and I fell a prey to perpetual horror. I hesitated to ride, or
vol2.txt:7777:been already too much an object for the scorn--for the horror--for the
vol2.txt:7804:am I not now dying a victim to the horror and the mystery of the wildest
vol2.txt:8148:possessed with an objectless yet intolerable horror. Gasping for
vol2.txt:8346:I say that I felt all the horrors of the damned? Most assuredly I had
vol2.txt:8392:from Oxford to the continent, in a perfect agony of horror and of shame.
vol2.txt:8491:astonishment, that horror which possessed me at the spectacle then
vol2.txt:8698:horror!-this I thought, and this I think. But anything was better than
vol2.txt:8958:dreams a cry as of horror and dismay; and thereunto, after a pause,
vol2.txt:8974:comprehension. Yet its memory was replete with horror--horror more
vol2.txt:9152:involved a penalty the exceeding great horror of which will not permit
vol3.txt:746:description. Every species of calamity and horror befell me. Among other
vol3.txt:897:My sensations were those of extreme horror and dismay. In vain I
vol3.txt:1086:horror with which I was inspired by the fragmentary warning thus
vol3.txt:1112:horrors which encompassed me. For another twenty-four hours it was
vol3.txt:1453:What was his grief and horror in discovering that the latter had
vol3.txt:2375:visitation, and that the appalling horror which has sometimes been
vol3.txt:2378:anticipative horror, lest the apparition might possibly be real, than
vol3.txt:2408:pitiable objects of horror and utter despair my eyes ever encountered.
vol3.txt:2605:us more fully the horrors which surrounded us. The brig was a mere
vol3.txt:2825:extremes first of delight and then of horror, than even any of the
vol3.txt:2899:of her decks. Shall I ever forget the triple horror of that spectacle?
vol3.txt:2907:raving with horror and despair--thoroughly mad through the anguish of
vol3.txt:3083:indescribable state of weakness and horror, brought on by the wine,
vol3.txt:3323:the tumultuous dangers of the storm or the gradually approaching horrors
vol3.txt:3376:horror of their reality. Let it suffice to say that, having in some
vol3.txt:3678:horror at the sound.
vol3.txt:5335:horror not to be tolerated--never to be conceived.
vol3.txt:5651:expressions of mingled horror, rage, and intense curiosity depicted
vol3.txt:5913:all imagined horrors crowding upon me in fact. I felt my knees strike
vol3.txt:5918:the cliff; and, with a wild, indefinable emotion, half of horror, half
vol3.txt:6884:unutterable horror and awe, for which the language of mortality has no
vol3.txt:6906:listened--in extremity of horror. The sound came again--it was a sigh.
vol3.txt:6928:horrors of that night? Why shall I pause to relate how, time after
vol3.txt:7021:horror, and the most beautiful became the most hideous, as Hinnon became
vol3.txt:7111:gloom, and horror, and grief swept over it in clouds. I said the child
vol3.txt:7143:and horror, for a worm that would not die.
vol3.txt:7487:an unaccountable sentiment of horror has hitherto prevented me from
vol3.txt:7507:altogether horrorless curiosity respecting yourself.
vol3.txt:7896:I stood petrified with horror and rage. I endeavored to reply, but my
vol3.txt:8652:the plunderer himself was often scared away by the horrors his own
vol3.txt:8668:footsteps must have been palsied by the horrors of their situation. The
vol3.txt:8787:manner, with a fit of what Tarpaulin called "the horrors." His jaws,
vol3.txt:8997:with bottles of junk. The man with the horrors was drowned upon the
vol4.txt:816:box with a blindfold impetuosity--but who shall describe his horror when
vol4.txt:1067:to the wall. To his extreme horror and astonishment, the head of the
vol4.txt:1229:recoil in horror from the deep and impressive meaning of his terrible
vol4.txt:1300:haste in the first place, and, in the second, a very usual horror at the
vol4.txt:2002:emotions of wonder and horror with which I gazed, when, leaping
vol4.txt:2622:my head gently to one side, I perceived, to my extreme horror, that the
vol4.txt:2675:But now a new horror presented itself, and one indeed sufficient to
vol4.txt:5004:insignificance, when to my extreme horror and astonishment I discovered
vol4.txt:5221:the belligerents, and throwing open the sash to their extreme horror and
vol4.txt:7736:terror, of horror, or of wo. You alone, habited in a white robe, passed
vol4.txt:8038:general lamentation and horror. This first sense of pain lay in a
vol4.txt:8059:details, of the fiery and horror-inspiring denunciations of the
vol4.txt:8166:And then did we, the seven, start from our seats in horror, and stand
vol5.txt:612:on its breast, with a feeling or horror and awe--with a sentiment of
vol5.txt:1057:shrieks of the multitude who gazed at them from below, horror-stricken,
vol5.txt:1099:takes up a burthen so heavy in horror that it can be thrown down only
vol5.txt:1874:seem to be rendered torpid, so that they have a horror of any thing like
vol5.txt:2235:room fainted outright through sheer horror. But after the first wild,
vol5.txt:4441:     And thy Angel I'll be, 'mid the horrors of this,--
vol5.txt:5252:             What a horror they outpour
vol5.txt:6923:  With horror and awe!
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
			
