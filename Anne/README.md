# Anne's work for Text IO 

## Homework

Array 1

```
>>> [0, 1, 2, 3]
[0, 1, 2, 3]
>>> reeks = [0, 1, 2, 3]
>>> reeks
[0, 1, 2, 3]
>>> naam = "Anne"
>>> vakken = ["Media Design", "Fotografie"]
>>> vakken
['Media Design', 'Fotografie']
>>> len(vakken)
2
>>> vakken.append("Graphic Design")
>>> len(vakken)
3
>>> vakken.pop()
'Graphic Design'
>>> len(vakken)
2
>>> print len(vakken)
2
>>> vakken = vakken + ["Graphic Design", "Philosophy"]
>>> len(vakken)
4
>>> vakken.pop()
'Philosophy'
>>> vakken.pop()
'Graphic Design'
>>> vakken.pop()
'Fotografie'
>>> 

```
Dictionary 1

```
>>> kamer={}
>>> kamer["adres"] = "Bredestraat 7"
>>> kamer["hoogte"] = "2.60 m"
>>> kamer["breedte"] = "3.50 m"
>>> kamer["lengte"] = "6.25 m"
>>> kamer["omtrek"] = "3.50 m x 6.25 m =21.88 m"
>>> kamer["deur"] = "2 x deur"
>>> kamer["raam"] = "2 x raam"
>>> kamer["kast"] = "3 x kast"
>>> print kamer
{'omtrek': '3.50 m x 6.25 m =21.88 m', 'raam': '2 x raam', 'adres': 'Bredestraat 7', 'kast': '3 x kast', 'breedte': '3.50 m', 'deur': '2 x deur', 'hoogte': '2.60 m', 'lengte': '6.25 m'}
>>>
 
```
Dictionary 2 

```

>>> huis = {'adres': "Bredestraat 7", 'huisdieren': 1, 'huur': 235}
>>> huis
{'huur': 235, 'huisdieren': 1, 'adres': 'Bredestraat 7'}
>>> huis['huisdieren']
1
>>> huis['huur']
235
>>> def maalvijf(x):
...     return x * 5
... 
>>> maalvijf(2)
10
>>> huis['huisdieren']
1
>>> huis['huisdieren'] = 3
>>> huis['huisdieren']
3
>>> huis
{'huur': 235, 'huisdieren': 3, 'adres': 'Bredestraat 7'}
>>> 
>>> ['huisdieren'] 
['huisdieren']

```

Data structure I


	}
		
		Album = {
	
	'artist': 'Earth, Wind & Fire',
	'album': 'I Am',
	'date' : '1979',
	'total': '9 songs',

	}

		{

		'name': 'In the Stone',
		'duration': '4:48',
		'prize': '0,99',

		},

		{
		
		'name': 'Cant Let Go',
		'duration': '3:28',
		'prize': '1,29',

		},

		{
		
		'name': 'After the Love Has Gone',
		'duration': '4:38',
		'prize': '0,99',

		},
		
		{
		
		'name': 'Let your Feelings Show',
		'duration': '5:13',
		'prize': '0,99',

		
		},
		
		{
		
		'name': 'Boogie Wonderland (with The Emotions)',
		'duration': '4:48',
		'prize': '0,99',


		},
		
		{
		
		'name': 'Star',
		'duration': '4:25',
		'prize': '0,99',

		},

		{
		
		'name': 'Wait',
		'duration': '3:39',
		'prize': '0,99',

		},

		{
		
		'name': 'Rock That!',
		'duration': '3:07',
		'prize': '0,99',

		},

		{
		
		'name': 'You and I',
		'duration': '3:32',
		'prize': '1,29',

		}


Data structure II font

	Font= {
	
	'font': 'Proxima Nova',
	'designer': 'Mark Simonson',
	'date': '2005',
	'weights': '14',


		{

		'weight': 'Thin',

		},

		{
		
		'weight': 'Thin italic',

		},

		{
		
		'weight': 'Light',

		},

		{
		
		'weight': 'Light italic',

		},

		{
		
		'weight': 'Regular',

		},

		{
		
		'weight': 'Regular italic',

		},

		{
		
		'weight': 'Semibold',

		},

		{
		
		'weight': 'Semibold italic',

		},

		{
	
		'weight': 'Bold',

		},

		{
		
		'weight': 'Bold italic',

		},

		{

		'weight': 'Extrabold',

		},

		{
		
		'weight': 'Extrabold italic',

		},

		{
		
		'weight': 'Black',

		},

		{
		
		'weight': 'Black italic',

		}


	Characters= {
	
	'Proxima Nova': 'fontfamily',

	}

		{
		'Leestekens': '.' , ? / . < > + = _ - ( ) # @ ! | \ ~ ® $ % & ¤ £ ¦ § ¥ ± ⁕ ⁋ ⁜ ⁂ ⁘ ⁙ ⁖ ⁚ • • № ℗ ℻ √',

		},

		{
		'Glyphs': 'À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ú Ù Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ Ā ā Ă ă Ą ą Ć ć Ĉ ĉ Ċ ċ Č č Ď ď Đ đ Ē ē Ĕ ĕ Ė ė Ę ę Ě ě Ĝ ĝ Ğ ğ Ġ ġ Ģ ģ Ĥ ĥ Ħ ħ Ĩ ĩ Ī ī Ĭ ĭ Į į İ ı Ĳ ĳ Ĵ ĵ Ķ ķ ĸ Ĺ ĺ Ļ ļ Ľ ľ Ŀ ŀ Ł ł Ń ń Ņ ņ Ň ň ŉ Ŋ ŋ Ō ō Ŏ ŏ Ő ő Œ œ Ŕ ŕ Ŗ ŗ Ř ř Ś ś Ŝ ŝ Ş ş Š š Ţ ţ Ť ť Ŧ ŧ Ũ ũ Ū ū Ŭ ŭ Ů ů Ű ű Ų ų Ŵ ŵ Ŷ ŷ Ÿ Ź ź Ż ż Ž ž ſ ƀ Ƃ ƃ Ɖ Ƌ ƌ ƍ Ǝ Ə Ɛ Ƒ ƒ Ɩ Ɨ ƚ ƛ Ɲ ƞ Ɵ Ơ ơ Ʀ Ƨ ƨ Ʃ Ʈ Ư ư Ʊ Ƶ ƶ Ʒ Ƹ ƹ ƻ ǀ ǁ ǂ ǃ Ǆ ǅ ǆ Ǉ ǈ ǉ Ǌ ǋ ǌ Ǎ ǎ Ǐ ǐ Ǒ ǒ Ǔ ǔ Ǖ ǖ Ǘ ǘ Ǚ ǚ Ǜ ǜ ǝ Ǟ ǟ Ǡ ǡ ǣ Ǣ ǣ Ǥ ǥ ǿ Ǧ ǧ Ǩ ǩ Ǫ ǫ Ǭ ǭ Ǯ ǯ ǰ Ǳ ǲ ǳ Ǵ ǵ Ƿ Ǹ ǹ Ǻ ǻ Ǽ ǽ Ǿ ǿ Ȁ ȁ Ȃ ȃ Ȅ ȅ Ȇ ȇ Ȉ ȉ Ȋ ȋ Ȍ ȍ Ȏ ȏ Ȑ ȑ Ȓ ȓ Ȕ ȕ Ȗ ȗ Ș ș Ⱥ Ț ʬ ʡ ɸ ɚ Ɇ Ɋ',

		},

		{
		'Cijfers': 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 

		}
		
		
	"Ankerpunten" = [

		{
		'Letter A': 

			'X:40.33', 'Y:20.67', 

			'X:64.91', 'Y:20.67',

			'X:100.39', 'Y:112.77',

			'X:78.16', 'Y:122.77',

			'X:72.36', 'Y:97.17',

			'X:32.87', 'Y:97.17',

			'X:27.07', 'Y:112.77',

			'X:4.84', 'Y:112.77'

		}

```
Cowsay

Last login: Thu Dec  3 12:22:52 on ttys001
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
It appears Homebrew is already installed. If your intent is to reinstall you
should do the following before running this installer again:
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
The current contents of /usr/local are bin CODEOFCONDUCT.md CONTRIBUTING.md Library LICENSE.txt README.md share SUPPORTERS.md .git .gitignore
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% brew install cowsay       [86]
==> Downloading https://homebrew.bintray.com/bottles/cowsay-3.03.yosemite.bottle
######################################################################### 100.0%
==> Pouring cowsay-3.03.yosemite.bottle.1.tar.gz
🍺  /usr/local/Cellar/cowsay/3.03: 53 files, 228K
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% cowsay "hello"            [87]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) n
 _______ 
< hello >
 ------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% cowsay -l                 [88]
Cow files in /usr/local/Cellar/cowsay/3.03/share/cows:
beavis.zen bong bud-frogs bunny cheese cower daemon default dragon
dragon-and-cow elephant elephant-in-snake eyes flaming-sheep ghostbusters
head-in hellokitty kiss kitty koala kosh luke-koala meow milk moofasa moose
mutilated ren satanic sheep skeleton small sodomized stegosaurus stimpy
supermilker surgery telebears three-eyes turkey turtle tux udder vader
vader-koala www
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% cowsay -f skeleton Hello  [89]
 _______ 
< Hello >
 ------- 
          \      (__)      
           \     /oo|  
            \   (_"_)*+++++++++*
                   //I#\\\\\\\\I\
                   I[I|I|||||I I `
                   I`I'///'' I I
                   I I       I I
                   ~ ~       ~ ~
                     Scowleton
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% 
```	 
	 
	 
	 
```
dict = {'naam': "Anne Goossens", 'age': 22}

    'GB-Datum': "07-05-1993",
    'GB-Plaats': "'s-Hertogenbosch", 
    'adres': "Groenstraat 51",
    'broer/zussen': 1 zus,
    'neven/nichten': 28,
    'ooms/tantes': 16, 	 
	 
```	 

```	
import my_data_file

d = my_data_file.my_dict

print "Hello, my name is %s I am %a years old" % (d['naam'], d['age']) 
	 
``` 
	 	 
 
Phone Home
 	 
``` 
Last login: Wed Jan  6 21:49:24 on ttys006
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% ps                       [165]
  PID TTY           TIME CMD
 1424 ttys000    0:00.01 -zsh
 1426 ttys001    0:00.10 -zsh
 1541 ttys002    0:00.08 -zsh
 2213 ttys003    0:00.07 -zsh
 1916 ttys004    0:00.09 -zsh
 2136 ttys004    0:00.00 cat
 2103 ttys006    0:00.07 -zsh
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% ps -ax.                  [166]
ps: illegal option -- .
usage: ps [-AaCcEefhjlMmrSTvwXx] [-O fmt | -o fmt] [-G gid[,gid...]]
          [-g grp[,grp...]] [-u [uid,uid...]]
          [-p pid[,pid...]] [-t tty[,tty...]] [-U user[,user...]]
       ps [-L]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% netstat -a |grep 'Adobe'
d1c7ab25949acb97 stream      0      0                0 d1c7ab25949acc5f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-AnneGoossens
d1c7ab25949acd27 stream      0      0                0 d1c7ab25949aceb7                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-AnneGoossens
d1c7ab25949ae497 stream      0      0                0 d1c7ab25949ae55f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-AnneGoossens
d1c7ab25949ae947 stream      0      0                0 d1c7ab25949aea0f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-AnneGoossens
d1c7ab25949ae627 stream      0      0                0 d1c7ab25949ae6ef                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-AnneGoossens
d1c7ab25949ae7b7 stream      0      0                0 d1c7ab25949ae87f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-AnneGoossens
d1c7ab25931b8d27 stream      0      0                0 d1c7ab25931b8def                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-AnneGoossens
d1c7ab25931b8eb7 stream      0      0                0 d1c7ab25931b8f7f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-AnneGoossens
d1c7ab25931b99a7 stream      0      0                0 d1c7ab25931b9d8f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-AnneGoossens
d1c7ab258f7c6557 stream      0      0                0 d1c7ab25931b9bff                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-AnneGoossens
d1c7ab258f7c67af stream      0      0 d1c7ab25939c01bf                0                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-AnneGoossens
d1c7ab25931ba55f stream      0      0                0 d1c7ab25931ba497                0                0 /Users/AnneGoossens/Library/Application Support/Adobe/Acrobat/DC/Acrobat/Synchronizer/Commands
d1c7ab25931ba87f stream      0      0 d1c7ab258fa1457f                0                0                0 /Users/AnneGoossens/Library/Application Support/Adobe/Acrobat/DC/Acrobat/Synchronizer/Notification
d1c7ab25931ba7b7 stream      0      0 d1c7ab25933b3cff                0                0                0 /Users/AnneGoossens/Library/Application Support/Adobe/Acrobat/DC/Acrobat/Synchronizer/Commands
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]%                                                      [168]
 
```
	 
```
Dictionary 3

Last login: Thu Nov 26 10:42:34 on ttys003
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% ls -al                     [1]
total 440
drwxr-xr-x+  41 AnneGoossens  staff   1394 Nov 26 11:10 ./
drwxr-xr-x    7 root          admin    238 Oct 29  2014 ../
-r--------    1 AnneGoossens  staff      7 Oct 29  2014 .CFUserTextEncoding
-rw-r--r--@   1 AnneGoossens  staff  14340 Nov 26 11:09 .DS_Store
drwx------  215 AnneGoossens  staff   7310 Nov 26 11:07 .Trash/
drwxr-xr-x    4 AnneGoossens  staff    136 Dec 29  2012 .adobe/
drwxr-x---    4 AnneGoossens  staff    136 May  4  2013 .android/
drwxr-xr-x   12 AnneGoossens  staff    408 Mar  9  2015 .atom/
-rw-------    1 AnneGoossens  staff    464 Nov 26 09:50 .bash_history
drwxr-xr-x    3 AnneGoossens  staff    102 Sep  5 12:47 .config/
drwx------    3 AnneGoossens  staff    102 Sep 22  2014 .cups/
drwx------   10 AnneGoossens  staff    340 Nov 26 09:32 .dropbox/
-rw-r--r--    1 AnneGoossens  staff    115 Sep 24 10:23 .gitconfig
-rw-r--r--    1 AnneGoossens  staff      0 Nov 26 09:53 .hiddenFile
drwxr-xr-x    3 AnneGoossens  staff    102 Oct  8 09:32 .python-eggs/
drwx------    5 AnneGoossens  staff    170 Sep 24 10:23 .ssh/
-rw-r--r--@   1 AnneGoossens  staff  32127 Nov 26  2012 .zcompdump
-rw-r--r--@   1 AnneGoossens  staff    461 Oct 31  2009 .zlogin
-rw-r--r--@   1 AnneGoossens  staff    150 Apr 17  2005 .zlogout
-rw-r--r--@   1 AnneGoossens  staff   1409 Nov 18  2014 .zprofile
drwxr-xr-x@   6 AnneGoossens  staff    204 Jun  1  2005 .zsh/
-rw-r--r--@   1 AnneGoossens  staff    254 Oct 31  2009 .zshenv
-rw-r--r--@   1 AnneGoossens  staff      0 Nov 18  2014 .zshhistory
-rw-r--r--@   1 AnneGoossens  staff  15704 Mar 28  2007 .zshrc
-rwxr-xr-x@   1 AnneGoossens  staff    512 Nov 18 17:58 .zshrc.local*
drwxr-xr-x    5 AnneGoossens  staff    170 Nov 19 13:36 Applications/
drwx------@   3 AnneGoossens  staff    102 Aug 24 10:57 Creative Cloud Files/
drwx------@   3 AnneGoossens  staff    102 Aug  8 20:48 Creative Cloud Files (1)/
drwx------+  50 AnneGoossens  staff   1700 Nov 26 11:09 Desktop/
drwx------+  16 AnneGoossens  staff    544 May 21  2015 Documents/
drwx------+  26 AnneGoossens  staff    884 Nov 26 11:08 Downloads/
drwx------@   8 AnneGoossens  staff    272 Nov 26 09:32 Dropbox/
drwx------@  57 AnneGoossens  staff   1938 Nov  3  2014 Library/
drwx------+   5 AnneGoossens  staff    170 Oct  1 10:40 Movies/
drwx------+   4 AnneGoossens  staff    136 Dec 27  2012 Music/
drwx------+  13 AnneGoossens  staff    442 Nov 14 16:18 Pictures/
drwxr-xr-x+   6 AnneGoossens  staff    204 Jul 28  2013 Public/
drwxr-xr-x+   6 AnneGoossens  staff    204 Jul 28  2013 Sites/
-rw-r--r--    1 AnneGoossens  staff  51240 Dec  8  2014 hs_err_pid443.log
drwx------@  11 AnneGoossens  staff    374 Nov 26 11:09 zsh_dotfiles/
-rw-r--r--@   1 AnneGoossens  staff  72209 Nov 26 10:26 zsh_dotfiles.tar
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% cd Downloads               [2]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Downloads]% cd..             [3]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% ls                         [4]
Applications/             Dropbox/                  Sites/
Creative Cloud Files/     Library/                  hs_err_pid443.log
Creative Cloud Files (1)/ Movies/                   zsh_dotfiles/
Desktop/                  Music/                    zsh_dotfiles.tar
Documents/                Pictures/
Downloads/                Public/
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% ls -l                      [4]
total 248
drwxr-xr-x   5 AnneGoossens  staff    170 Nov 19 13:36 Applications/
drwx------@  3 AnneGoossens  staff    102 Aug 24 10:57 Creative Cloud Files/
drwx------@  3 AnneGoossens  staff    102 Aug  8 20:48 Creative Cloud Files (1)/
drwx------+ 50 AnneGoossens  staff   1700 Nov 26 11:09 Desktop/
drwx------+ 16 AnneGoossens  staff    544 May 21  2015 Documents/
drwx------+ 26 AnneGoossens  staff    884 Nov 26 11:08 Downloads/
drwx------@  8 AnneGoossens  staff    272 Nov 26 09:32 Dropbox/
drwx------@ 57 AnneGoossens  staff   1938 Nov  3  2014 Library/
drwx------+  5 AnneGoossens  staff    170 Oct  1 10:40 Movies/
drwx------+  4 AnneGoossens  staff    136 Dec 27  2012 Music/
drwx------+ 13 AnneGoossens  staff    442 Nov 14 16:18 Pictures/
drwxr-xr-x+  6 AnneGoossens  staff    204 Jul 28  2013 Public/
drwxr-xr-x+  6 AnneGoossens  staff    204 Jul 28  2013 Sites/
-rw-r--r--   1 AnneGoossens  staff  51240 Dec  8  2014 hs_err_pid443.log
drwx------@ 11 AnneGoossens  staff    374 Nov 26 11:09 zsh_dotfiles/
-rw-r--r--@  1 AnneGoossens  staff  72209 Nov 26 10:26 zsh_dotfiles.tar
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% l                          [5]
total 248
drwxr-xr-x   5 AnneGoossens  staff   170B Nov 19 13:36 Applications/
drwx------@  3 AnneGoossens  staff   102B Aug 24 10:57 Creative Cloud Files/
drwx------@  3 AnneGoossens  staff   102B Aug  8 20:48 Creative Cloud Files (1)/
drwx------+ 50 AnneGoossens  staff   1.7K Nov 26 11:09 Desktop/
drwx------+ 16 AnneGoossens  staff   544B May 21  2015 Documents/
drwx------+ 26 AnneGoossens  staff   884B Nov 26 11:08 Downloads/
drwx------@  8 AnneGoossens  staff   272B Nov 26 09:32 Dropbox/
drwx------@ 57 AnneGoossens  staff   1.9K Nov  3  2014 Library/
drwx------+  5 AnneGoossens  staff   170B Oct  1 10:40 Movies/
drwx------+  4 AnneGoossens  staff   136B Dec 27  2012 Music/
drwx------+ 13 AnneGoossens  staff   442B Nov 14 16:18 Pictures/
drwxr-xr-x+  6 AnneGoossens  staff   204B Jul 28  2013 Public/
drwxr-xr-x+  6 AnneGoossens  staff   204B Jul 28  2013 Sites/
-rw-r--r--   1 AnneGoossens  staff    50K Dec  8  2014 hs_err_pid443.log
drwx------@ 11 AnneGoossens  staff   374B Nov 26 11:09 zsh_dotfiles/
-rw-r--r--@  1 AnneGoossens  staff    71K Nov 26 10:26 zsh_dotfiles.tar
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% ll                         [6]
total 448
drwxr-xr-x+  41 AnneGoossens  staff   1.4K Nov 26 11:17 ./
drwxr-xr-x    7 root          admin   238B Oct 29  2014 ../
-r--------    1 AnneGoossens  staff     7B Oct 29  2014 .CFUserTextEncoding
-rw-r--r--@   1 AnneGoossens  staff    14K Nov 26 11:09 .DS_Store
drwx------  215 AnneGoossens  staff   7.1K Nov 26 11:07 .Trash/
drwxr-xr-x    4 AnneGoossens  staff   136B Dec 29  2012 .adobe/
drwxr-x---    4 AnneGoossens  staff   136B May  4  2013 .android/
drwxr-xr-x   12 AnneGoossens  staff   408B Mar  9  2015 .atom/
-rw-------    1 AnneGoossens  staff   464B Nov 26 09:50 .bash_history
drwxr-xr-x    3 AnneGoossens  staff   102B Sep  5 12:47 .config/
drwx------    3 AnneGoossens  staff   102B Sep 22  2014 .cups/
drwx------   10 AnneGoossens  staff   340B Nov 26 09:32 .dropbox/
-rw-r--r--    1 AnneGoossens  staff   115B Sep 24 10:23 .gitconfig
-rw-r--r--    1 AnneGoossens  staff     0B Nov 26 09:53 .hiddenFile
drwxr-xr-x    3 AnneGoossens  staff   102B Oct  8 09:32 .python-eggs/
drwx------    5 AnneGoossens  staff   170B Sep 24 10:23 .ssh/
-rw-r--r--@   1 AnneGoossens  staff    31K Nov 26  2012 .zcompdump
-rw-r--r--@   1 AnneGoossens  staff   461B Oct 31  2009 .zlogin
-rw-r--r--@   1 AnneGoossens  staff   150B Apr 17  2005 .zlogout
-rw-r--r--@   1 AnneGoossens  staff   1.4K Nov 18  2014 .zprofile
drwxr-xr-x@   6 AnneGoossens  staff   204B Jun  1  2005 .zsh/
-rw-r--r--@   1 AnneGoossens  staff   254B Oct 31  2009 .zshenv
-rw-r--r--@   1 AnneGoossens  staff   106B Nov 26 11:17 .zshhistory
-rw-r--r--@   1 AnneGoossens  staff    15K Mar 28  2007 .zshrc
-rwxr-xr-x@   1 AnneGoossens  staff   512B Nov 18 17:58 .zshrc.local*
drwxr-xr-x    5 AnneGoossens  staff   170B Nov 19 13:36 Applications/
drwx------@   3 AnneGoossens  staff   102B Aug 24 10:57 Creative Cloud Files/
drwx------@   3 AnneGoossens  staff   102B Aug  8 20:48 Creative Cloud Files (1)/
drwx------+  50 AnneGoossens  staff   1.7K Nov 26 11:09 Desktop/
drwx------+  16 AnneGoossens  staff   544B May 21  2015 Documents/
drwx------+  26 AnneGoossens  staff   884B Nov 26 11:08 Downloads/
drwx------@   8 AnneGoossens  staff   272B Nov 26 09:32 Dropbox/
drwx------@  57 AnneGoossens  staff   1.9K Nov  3  2014 Library/
drwx------+   5 AnneGoossens  staff   170B Oct  1 10:40 Movies/
drwx------+   4 AnneGoossens  staff   136B Dec 27  2012 Music/
drwx------+  13 AnneGoossens  staff   442B Nov 14 16:18 Pictures/
drwxr-xr-x+   6 AnneGoossens  staff   204B Jul 28  2013 Public/
drwxr-xr-x+   6 AnneGoossens  staff   204B Jul 28  2013 Sites/
-rw-r--r--    1 AnneGoossens  staff    50K Dec  8  2014 hs_err_pid443.log
drwx------@  11 AnneGoossens  staff   374B Nov 26 11:09 zsh_dotfiles/
-rw-r--r--@   1 AnneGoossens  staff    71K Nov 26 10:26 zsh_dotfiles.tar
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% pwd                        [7]
/Users/AnneGoossens
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% mkdir FolderNaam           [8]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% l                          [8]
total 248
drwxr-xr-x   5 AnneGoossens  staff   170B Nov 19 13:36 Applications/
drwx------@  3 AnneGoossens  staff   102B Aug 24 10:57 Creative Cloud Files/
drwx------@  3 AnneGoossens  staff   102B Aug  8 20:48 Creative Cloud Files (1)/
drwx------+ 50 AnneGoossens  staff   1.7K Nov 26 11:09 Desktop/
drwx------+ 16 AnneGoossens  staff   544B May 21  2015 Documents/
drwx------+ 26 AnneGoossens  staff   884B Nov 26 11:08 Downloads/
drwx------@  8 AnneGoossens  staff   272B Nov 26 09:32 Dropbox/
drwxr-xr-x   2 AnneGoossens  staff    68B Nov 26 11:19 FolderNaam/
drwx------@ 57 AnneGoossens  staff   1.9K Nov  3  2014 Library/
drwx------+  5 AnneGoossens  staff   170B Oct  1 10:40 Movies/
drwx------+  4 AnneGoossens  staff   136B Dec 27  2012 Music/
drwx------+ 13 AnneGoossens  staff   442B Nov 14 16:18 Pictures/
drwxr-xr-x+  6 AnneGoossens  staff   204B Jul 28  2013 Public/
drwxr-xr-x+  6 AnneGoossens  staff   204B Jul 28  2013 Sites/
-rw-r--r--   1 AnneGoossens  staff    50K Dec  8  2014 hs_err_pid443.log
drwx------@ 11 AnneGoossens  staff   374B Nov 26 11:09 zsh_dotfiles/
-rw-r--r--@  1 AnneGoossens  staff    71K Nov 26 10:26 zsh_dotfiles.tar
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% cd FolderNaam              [9]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/FolderNaam]% pwd            [10]
/Users/AnneGoossens/FolderNaam
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/FolderNaam]% cd ~           [11]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% cd Downloads/FolderNaam   [11]
cd: no such file or directory: Downloads/FolderNaam
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% cd /                      [12]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: /]% pwd                       [13]
/
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: /]% cd ~                      [14]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% cd /System/Library/       [14]
---- directory
Accessibility/            Image\ Capture/             Receipts/          
Accounts/                 Input\ Methods/             Recents/           
Address\ Book\ Plug-Ins/  InternetAccounts/           SDKSettingsPlist/  
Assistant/                Java/                       Sandbox/           
Automator/                KerberosPlugins/            Screen\ Savers/    
BridgeSupport/            Kernels/                    ScreenReader/      
CacheDelete/              Keyboard\ Layouts/          ScriptingAdditions/
Caches/                   Keychains/                  ScriptingDefinitions/
ColorPickers/             LaunchAgents/               Security/          
ColorSync/                LaunchDaemons/              Services/          
Colors/                   LinguisticData/             Sounds/            
Components/               LocationBundles/            Speech/            
Compositions/             LoginPlugins/               Spelling/          
ConfigurationProfiles/    Messages/                   Spotlight/         
CoreServices/             Metadata/                   StagedFrameworks/  
CryptoTokenKit/           MonitorPanels/              StartupItems/      
DTDs/                     OpenDirectory/              SyncServices/      
DirectoryServices/        OpenSSL/                    SystemConfiguration/
Displays/                 Password\ Server\ Filters/  SystemProfiler/    
Extensions/               Perl/                       Tcl/               
Filesystems/              PreferencePanes/            TextEncodings/     
Filters/                  PrelinkedKernels/           User\ Template/    
Fonts/                    Printers/                   UserEventPlugins/  
Frameworks/               PrivateFrameworks/          Video/             
Graphics/                 QuickLook/                  WidgetResources/   
IdentityServices/         QuickTime/                                     
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~]% cd /System/Library/Fonts  [14]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: /System/Library/Fonts]% l     [15]
total 424968
-rw-r--r--  1 root  wheel   258K Sep 10  2014 Apple Braille Outline 6 Dot.ttf
-rw-r--r--  1 root  wheel   274K Sep 10  2014 Apple Braille Outline 8 Dot.ttf
-rw-r--r--  1 root  wheel   179K Sep 10  2014 Apple Braille Pinpoint 6 Dot.ttf
-rw-r--r--  1 root  wheel   185K Sep 10  2014 Apple Braille Pinpoint 8 Dot.ttf
-rw-r--r--  1 root  wheel   133K Sep 10  2014 Apple Braille.ttf
-rw-r--r--  1 root  wheel    55M Mar 19  2015 Apple Color Emoji.ttf
-rw-r--r--  1 root  wheel   1.6M Sep 10  2014 Apple Symbols.ttc
-rw-r--r--  1 root  wheel   3.5M Sep 10  2014 AppleSDGothicNeo-Bold.otf
-rw-r--r--  1 root  wheel   3.2M Sep 10  2014 AppleSDGothicNeo-Regular.otf
-rw-r--r--  1 root  wheel    18M Sep 10  2014 AquaKana.ttc
-rw-r--r--  1 root  wheel   188K Sep 10  2014 ArialHB.ttc
-rw-r--r--  1 root  wheel   3.0M Sep 10  2014 Avenir Next Condensed.ttc
-rw-r--r--  1 root  wheel   4.9M Sep 10  2014 Avenir Next.ttc
-rw-r--r--  1 root  wheel   1.5M Sep 10  2014 Avenir.ttc
-rw-r--r--  1 root  wheel   1.3M Sep 10  2014 Courier.dfont
-rw-r--r--  1 root  wheel   971K Sep 10  2014 GeezaPro.ttc
-rw-r--r--  1 root  wheel   721K Sep 10  2014 Geneva.dfont
-rw-r--r--@ 1 root  wheel     0B Sep 10  2014 HelveLTMM
-rw-r--r--@ 1 root  wheel     0B Sep 10  2014 Helvetica LT MM
-rw-r--r--  1 root  wheel   2.4M Sep 10  2014 Helvetica.dfont
-rw-r--r--  1 root  wheel   6.4M Sep 10  2014 HelveticaNeue.dfont
-rw-r--r--  1 root  wheel   5.1M Sep 10  2014 HelveticaNeueDeskInterface.ttc
-rw-r--r--  1 root  wheel   3.5M Sep 10  2014 HiraKakuInterface-W1.otf
-rw-r--r--  1 root  wheel   3.5M Sep 10  2014 HiraKakuInterface-W2.otf
-rw-r--r--  1 root  wheel    34K Sep 10  2014 Keyboard.ttf
-rw-r--r--  1 root  wheel   896K Sep 10  2014 Kohinoor.ttc
-rw-r--r--  1 root  wheel   691K Sep 10  2014 LastResort.ttf
-rw-r--r--  1 root  wheel   3.0M Sep 10  2014 LucidaGrande.ttc
-rw-r--r--  1 root  wheel   607K Sep 10  2014 MarkerFelt.ttc
-rw-r--r--  1 root  wheel   2.0M Sep 10  2014 Menlo.ttc
-rw-r--r--  1 root  wheel   551K Sep 10  2014 Monaco.dfont
-rw-r--r--  1 root  wheel   539K Sep 10  2014 Noteworthy.ttc
-rw-r--r--  1 root  wheel   554K Sep 10  2014 Optima.ttc
-rw-r--r--  1 root  wheel   1.6M Sep 10  2014 Palatino.ttc
-rw-r--r--  1 root  wheel    53M Sep 10  2014 STHeiti Light.ttc
-rw-r--r--  1 root  wheel    53M Sep 10  2014 STHeiti Medium.ttc
-rw-r--r--  1 root  wheel   7.7M Sep 10  2014 STHeiti Thin.ttc
-rw-r--r--  1 root  wheel   8.0M Sep 10  2014 STHeiti UltraLight.ttc
-rw-r--r--  1 root  wheel   101K Sep 10  2014 Symbol.ttf
-rw-r--r--  1 root  wheel   2.3M Sep 10  2014 Thonburi.ttc
-rw-r--r--@ 1 root  wheel     0B Sep 10  2014 Times LT MM
-rw-r--r--  1 root  wheel   1.5M Sep 10  2014 Times.dfont
-rw-r--r--@ 1 root  wheel     0B Sep 10  2014 TimesLTMM
-rw-r--r--  1 root  wheel   151K Sep 10  2014 ZapfDingbats.ttf
-rw-r--r--  1 root  wheel    10M Sep 10  2014 ヒラギノ明朝 ProN W3.otf
-rw-r--r--  1 root  wheel    10M Sep 10  2014 ヒラギノ明朝 ProN W6.otf
-rw-r--r--  1 root  wheel   7.1M Sep 10  2014 ヒラギノ角ゴ ProN W3.otf
-rw-r--r--  1 root  wheel   7.2M Sep 10  2014 ヒラギノ角ゴ ProN W6.otf
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: /System/Library/Fonts]% ll    [16]
total 424968
drwxr-xr-x  50 root  wheel   1.7K Nov 18 11:34 ./
drwxr-xr-x  80 root  wheel   2.7K Sep 24 11:22 ../
-rw-r--r--   1 root  wheel   258K Sep 10  2014 Apple Braille Outline 6 Dot.ttf
-rw-r--r--   1 root  wheel   274K Sep 10  2014 Apple Braille Outline 8 Dot.ttf
-rw-r--r--   1 root  wheel   179K Sep 10  2014 Apple Braille Pinpoint 6 Dot.ttf
-rw-r--r--   1 root  wheel   185K Sep 10  2014 Apple Braille Pinpoint 8 Dot.ttf
-rw-r--r--   1 root  wheel   133K Sep 10  2014 Apple Braille.ttf
-rw-r--r--   1 root  wheel    55M Mar 19  2015 Apple Color Emoji.ttf
-rw-r--r--   1 root  wheel   1.6M Sep 10  2014 Apple Symbols.ttc
-rw-r--r--   1 root  wheel   3.5M Sep 10  2014 AppleSDGothicNeo-Bold.otf
-rw-r--r--   1 root  wheel   3.2M Sep 10  2014 AppleSDGothicNeo-Regular.otf
-rw-r--r--   1 root  wheel    18M Sep 10  2014 AquaKana.ttc
-rw-r--r--   1 root  wheel   188K Sep 10  2014 ArialHB.ttc
-rw-r--r--   1 root  wheel   3.0M Sep 10  2014 Avenir Next Condensed.ttc
-rw-r--r--   1 root  wheel   4.9M Sep 10  2014 Avenir Next.ttc
-rw-r--r--   1 root  wheel   1.5M Sep 10  2014 Avenir.ttc
-rw-r--r--   1 root  wheel   1.3M Sep 10  2014 Courier.dfont
-rw-r--r--   1 root  wheel   971K Sep 10  2014 GeezaPro.ttc
-rw-r--r--   1 root  wheel   721K Sep 10  2014 Geneva.dfont
-rw-r--r--@  1 root  wheel     0B Sep 10  2014 HelveLTMM
-rw-r--r--@  1 root  wheel     0B Sep 10  2014 Helvetica LT MM
-rw-r--r--   1 root  wheel   2.4M Sep 10  2014 Helvetica.dfont
-rw-r--r--   1 root  wheel   6.4M Sep 10  2014 HelveticaNeue.dfont
-rw-r--r--   1 root  wheel   5.1M Sep 10  2014 HelveticaNeueDeskInterface.ttc
-rw-r--r--   1 root  wheel   3.5M Sep 10  2014 HiraKakuInterface-W1.otf
-rw-r--r--   1 root  wheel   3.5M Sep 10  2014 HiraKakuInterface-W2.otf
-rw-r--r--   1 root  wheel    34K Sep 10  2014 Keyboard.ttf
-rw-r--r--   1 root  wheel   896K Sep 10  2014 Kohinoor.ttc
-rw-r--r--   1 root  wheel   691K Sep 10  2014 LastResort.ttf
-rw-r--r--   1 root  wheel   3.0M Sep 10  2014 LucidaGrande.ttc
-rw-r--r--   1 root  wheel   607K Sep 10  2014 MarkerFelt.ttc
-rw-r--r--   1 root  wheel   2.0M Sep 10  2014 Menlo.ttc
-rw-r--r--   1 root  wheel   551K Sep 10  2014 Monaco.dfont
-rw-r--r--   1 root  wheel   539K Sep 10  2014 Noteworthy.ttc
-rw-r--r--   1 root  wheel   554K Sep 10  2014 Optima.ttc
-rw-r--r--   1 root  wheel   1.6M Sep 10  2014 Palatino.ttc
-rw-r--r--   1 root  wheel    53M Sep 10  2014 STHeiti Light.ttc
-rw-r--r--   1 root  wheel    53M Sep 10  2014 STHeiti Medium.ttc
-rw-r--r--   1 root  wheel   7.7M Sep 10  2014 STHeiti Thin.ttc
-rw-r--r--   1 root  wheel   8.0M Sep 10  2014 STHeiti UltraLight.ttc
-rw-r--r--   1 root  wheel   101K Sep 10  2014 Symbol.ttf
-rw-r--r--   1 root  wheel   2.3M Sep 10  2014 Thonburi.ttc
-rw-r--r--@  1 root  wheel     0B Sep 10  2014 Times LT MM
-rw-r--r--   1 root  wheel   1.5M Sep 10  2014 Times.dfont
-rw-r--r--@  1 root  wheel     0B Sep 10  2014 TimesLTMM
-rw-r--r--   1 root  wheel   151K Sep 10  2014 ZapfDingbats.ttf
-rw-r--r--   1 root  wheel    10M Sep 10  2014 ヒラギノ明朝 ProN W3.otf
-rw-r--r--   1 root  wheel    10M Sep 10  2014 ヒラギノ明朝 ProN W6.otf
-rw-r--r--   1 root  wheel   7.1M Sep 10  2014 ヒラギノ角ゴ ProN W3.otf
-rw-r--r--   1 root  wheel   7.2M Sep 10  2014 ヒラギノ角ゴ ProN W6.otf
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: /System/Library/Fonts]% d     [17]
0	/System/Library/Fonts
1	~
2	/
3	~/FolderNaam
4	~/Downloads
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: /System/Library/Fonts]% 3     [18]
~/FolderNaam
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/FolderNaam]% cd -           [18]
/System/Library/Fonts
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: /System/Library/Fonts]% ls M*
MarkerFelt.ttc  Menlo.ttc       Monaco.dfont
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: /System/Library/Fonts]% ls M?nlo.*
Menlo.ttc
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: /System/Library/Fonts]% cd ~/D
cd: no such file or directory: /Users/AnneGoossens/D
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: /System/Library/Fonts]% cd ~/Downloads
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Downloads]% l               [22]
total 199352
drwx------@  6 AnneGoossens  staff   204B Nov 16 10:10 Dagboek/
drwx------@  5 AnneGoossens  staff   170B Nov 16 10:10 Dagboek-2/
drwxr-xr-x@  6 AnneGoossens  staff   204B Nov 15 17:38 ESSAY 2 MEDIA/
drwxr-xr-x@  3 AnneGoossens  staff   102B Nov  1 20:18 FILOSOFIE/
-rw-r--r--@  1 AnneGoossens  staff    86M May 22  2015 GoogleEarthMac-Intel.dmg
drwxr-xr-x@  3 AnneGoossens  staff   102B Oct 19  2014 Mou.app/
drwx------@  4 AnneGoossens  staff   136B Nov 14 18:09 Outlook/
drwx------@  5 AnneGoossens  staff   170B Nov 14 18:13 Outlook-2/
drwxr-xr-x@ 36 AnneGoossens  staff   1.2K Nov 18 16:33 SREENSHOTS/
drwxr-xr-x@ 17 AnneGoossens  staff   578B Nov 12 23:29 THE TRUMAN SHOW/
-rw-r--r--@  1 AnneGoossens  staff   5.6M Nov 19 23:20 The Truman Show 2.indd
-rw-r--r--@  1 AnneGoossens  staff   5.6M Nov 19 23:20 The Truman Show.indd
drwx------@ 10 AnneGoossens  staff   340B Nov 13 09:42 Typo/
drwx------@  7 AnneGoossens  staff   238B Nov 13 09:46 Typo 2/
drwx------@ 12 AnneGoossens  staff   408B Nov 13 11:36 Typo 4/
drwx------@  7 AnneGoossens  staff   238B Nov 13 09:43 Typo-2/
drwx------@ 11 AnneGoossens  staff   374B Nov 13 11:37 Typo-3/
drwx------@  6 AnneGoossens  staff   204B Nov 13 11:39 Typo5/
drwx------@ 11 AnneGoossens  staff   374B Nov 26 10:27 zsh_dotfiles/
drwx------@ 11 AnneGoossens  staff   374B Nov 26 10:27 zsh_dotfiles 2/
-rw-r--r--@  1 AnneGoossens  staff    71K Nov 26 10:58 zsh_dotfiles-2.tar
-rw-r--r--@  1 AnneGoossens  staff    71K Nov 26 11:08 zsh_dotfiles.tar
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Downloads]% mv zsh_testfiles.tar
usage: mv [-f | -i | -n] [-v] source target
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Downloads]% mv zsh_testfiles.tar ~/Documents/        [24]
mv: zsh_testfiles.tar: No such file or directory
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Downloads]% history                                  [25]
    4  ls -l
    7  mkdir FolderNaam
    9  cd FolderNaam
   11  cd Downloads/FolderNaam
   12  cd /
   13  cd ~
   14  cd /System/Library/Fonts
   16  ll
   17  cd -
   18  ls M*
   19  ls M?nlo.*
   20  cd ~/D
   21  cd ~/Downloads
   22  l
   23  mv zsh_testfiles.tar
   24  mv zsh_testfiles.tar ~/Documents/
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Downloads]% ls ~/Documents/                          [26]
?Post.docx
AIGA.docx
ANNE
Adobe/
Adobe Flash Builder 4.6/
Handleiding_Souvenir.docx
Microsoft User Data/
Naamloos-1.ai
Plattegrond_Rietveld.pdf
Processing/
RDC Connections/
Zijn ontwerpen waren een aanklacht tegen het kapitalisme en de industriële revolutie.docx
zsh_testfiles.tar
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Downloads]% cd ~/Documents/                          [27]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents]% l                                        [28]
total 5368
-rw-r--r--@ 1 AnneGoossens  staff    28K May 21  2015 ?Post.docx
-rw-r--r--@ 1 AnneGoossens  staff    30K Feb  9  2015 AIGA.docx
-rw-r--r--@ 1 AnneGoossens  staff   1.1M May 21  2015 ANNE
drwxrwxr-x  7 AnneGoossens  staff   238B Nov 12 13:43 Adobe/
drwxrwxr-x  4 AnneGoossens  staff   136B May 11  2014 Adobe Flash Builder 4.6/
-rw-r--r--@ 1 AnneGoossens  staff    40K Mar 31  2015 Handleiding_Souvenir.docx
drwxr-xr-x  9 AnneGoossens  staff   306B Dec 29  2012 Microsoft User Data/
-rw-r--r--@ 1 AnneGoossens  staff   1.3M Sep 23  2014 Naamloos-1.ai
-rw-r--r--@ 1 AnneGoossens  staff    41K Jan 21  2015 Plattegrond_Rietveld.pdf
drwxr-xr-x  5 AnneGoossens  staff   170B Sep  8  2014 Processing/
drwxr-xr-x  4 AnneGoossens  staff   136B Sep  6  2014 RDC Connections/
-rw-r--r--@ 1 AnneGoossens  staff   131K Dec 15  2014 Zijn ontwerpen waren een aanklacht tegen het kapitalisme en de industriële revolutie.docx
-rw-r--r--@ 1 AnneGoossens  staff   745B Nov 26 11:38 zsh_testfiles.tar
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents]% tar -xzf zsh_testfiles.tar               [29]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents]% cd Testfiles                             [30]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% l                              [31]
total 152
-rw-r--r--@ 1 AnneGoossens  staff    17B Nov 26 10:24 april.txt
-rw-r--r--@ 1 AnneGoossens  staff    18B Nov 26 10:25 august.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 december.txt
-rw-r--r--@ 1 AnneGoossens  staff    20B Nov 26 10:24 february.txt
-rw-r--r--@ 1 AnneGoossens  staff     7B Nov 26 08:58 friday.txt
-rw-r--r--@ 1 AnneGoossens  staff    30B Nov 26 10:23 january.txt
-rw-r--r--@ 1 AnneGoossens  staff    16B Nov 26 10:25 july.txt
-rw-r--r--@ 1 AnneGoossens  staff    16B Nov 26 10:25 june.txt
-rw-r--r--@ 1 AnneGoossens  staff    17B Nov 26 10:24 march.txt
-rw-r--r--@ 1 AnneGoossens  staff    15B Nov 26 10:25 may.txt
-rw-r--r--@ 1 AnneGoossens  staff     7B Nov 26 08:57 monday.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 november.txt
-rw-r--r--@ 1 AnneGoossens  staff    20B Nov 26 10:26 october.txt
-rw-r--r--@ 1 AnneGoossens  staff     9B Nov 26 08:58 saturday.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 september.txt
-rw-r--r--@ 1 AnneGoossens  staff     7B Nov 26 08:58 sunday.txt
-rw-r--r--@ 1 AnneGoossens  staff     9B Nov 26 08:58 thursday.txt
-rw-r--r--@ 1 AnneGoossens  staff     8B Nov 26 08:57 tuesday.txt
-rw-r--r--@ 1 AnneGoossens  staff    10B Nov 26 08:57 wednesday.txt
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% cd /Users/AnneGoossens/Documents 
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents]% open .                                   [33]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents]% cd Testfiles                             [34]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% l                              [35]
total 152
-rw-r--r--@ 1 AnneGoossens  staff    17B Nov 26 10:24 april.txt
-rw-r--r--@ 1 AnneGoossens  staff    18B Nov 26 10:25 august.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 december.txt
-rw-r--r--@ 1 AnneGoossens  staff    20B Nov 26 10:24 february.txt
-rw-r--r--@ 1 AnneGoossens  staff     7B Nov 26 08:58 friday.txt
-rw-r--r--@ 1 AnneGoossens  staff    30B Nov 26 10:23 january.txt
-rw-r--r--@ 1 AnneGoossens  staff    16B Nov 26 10:25 july.txt
-rw-r--r--@ 1 AnneGoossens  staff    16B Nov 26 10:25 june.txt
-rw-r--r--@ 1 AnneGoossens  staff    17B Nov 26 10:24 march.txt
-rw-r--r--@ 1 AnneGoossens  staff    15B Nov 26 10:25 may.txt
-rw-r--r--@ 1 AnneGoossens  staff     7B Nov 26 08:57 monday.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 november.txt
-rw-r--r--@ 1 AnneGoossens  staff    20B Nov 26 10:26 october.txt
-rw-r--r--@ 1 AnneGoossens  staff     9B Nov 26 08:58 saturday.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 september.txt
-rw-r--r--@ 1 AnneGoossens  staff     7B Nov 26 08:58 sunday.txt
-rw-r--r--@ 1 AnneGoossens  staff     9B Nov 26 08:58 thursday.txt
-rw-r--r--@ 1 AnneGoossens  staff     8B Nov 26 08:57 tuesday.txt
-rw-r--r--@ 1 AnneGoossens  staff    10B Nov 26 08:57 wednesday.txt
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% l | pbcopy                     [36]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% cat tuesday.txt                [37]
Tuesday
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% cat `pbpaste`                  [38]
cat: wedneday.txt: No such file or directory
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% open .                         [39]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% cat april.txt                  [40]
Month 4 is April
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% cat april.txt may.txt june.txt
Month 4 is April
Month 5 is May
Month 6 is June
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% cat *.txt                      [42]
Month 4 is April
Month 8 is August
Month 12 is December
Month 2 is February
Friday
File for the month of January
Month 7 is July
Month 6 is June
Month 3 is March
Month 5 is May
Monday
Month 11 is November
Month 10 is October
Saturday
Month 9 is September
Sunday
Thursday
Tuesday
Wednesday
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% mkdir Days                     [43]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% l                              [44]
total 152
drwxr-xr-x  2 AnneGoossens  staff    68B Nov 26 12:09 Days/
-rw-r--r--@ 1 AnneGoossens  staff    17B Nov 26 10:24 april.txt
-rw-r--r--@ 1 AnneGoossens  staff    18B Nov 26 10:25 august.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 december.txt
-rw-r--r--@ 1 AnneGoossens  staff    20B Nov 26 10:24 february.txt
-rw-r--r--@ 1 AnneGoossens  staff     7B Nov 26 08:58 friday.txt
-rw-r--r--@ 1 AnneGoossens  staff    30B Nov 26 10:23 january.txt
-rw-r--r--@ 1 AnneGoossens  staff    16B Nov 26 10:25 july.txt
-rw-r--r--@ 1 AnneGoossens  staff    16B Nov 26 10:25 june.txt
-rw-r--r--@ 1 AnneGoossens  staff    17B Nov 26 10:24 march.txt
-rw-r--r--@ 1 AnneGoossens  staff    15B Nov 26 10:25 may.txt
-rw-r--r--@ 1 AnneGoossens  staff     7B Nov 26 08:57 monday.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 november.txt
-rw-r--r--@ 1 AnneGoossens  staff    20B Nov 26 10:26 october.txt
-rw-r--r--@ 1 AnneGoossens  staff     9B Nov 26 08:58 saturday.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 september.txt
-rw-r--r--@ 1 AnneGoossens  staff     7B Nov 26 08:58 sunday.txt
-rw-r--r--@ 1 AnneGoossens  staff     9B Nov 26 08:58 thursday.txt
-rw-r--r--@ 1 AnneGoossens  staff     8B Nov 26 08:57 tuesday.txt
-rw-r--r--@ 1 AnneGoossens  staff    10B Nov 26 08:57 wednesday.txt
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% mv *day.txt Days/              [45]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% l                              [46]
total 96
drwxr-xr-x  9 AnneGoossens  staff   306B Nov 26 12:11 Days/
-rw-r--r--@ 1 AnneGoossens  staff    17B Nov 26 10:24 april.txt
-rw-r--r--@ 1 AnneGoossens  staff    18B Nov 26 10:25 august.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 december.txt
-rw-r--r--@ 1 AnneGoossens  staff    20B Nov 26 10:24 february.txt
-rw-r--r--@ 1 AnneGoossens  staff    30B Nov 26 10:23 january.txt
-rw-r--r--@ 1 AnneGoossens  staff    16B Nov 26 10:25 july.txt
-rw-r--r--@ 1 AnneGoossens  staff    16B Nov 26 10:25 june.txt
-rw-r--r--@ 1 AnneGoossens  staff    17B Nov 26 10:24 march.txt
-rw-r--r--@ 1 AnneGoossens  staff    15B Nov 26 10:25 may.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 november.txt
-rw-r--r--@ 1 AnneGoossens  staff    20B Nov 26 10:26 october.txt
-rw-r--r--@ 1 AnneGoossens  staff    21B Nov 26 10:26 september.txt
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% mkdir Months                   [47]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% mv *txt Months/                [48]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% l                              [49]
total 0
drwxr-xr-x   9 AnneGoossens  staff   306B Nov 26 12:11 Days/
drwxr-xr-x  14 AnneGoossens  staff   476B Nov 26 12:12 Months/
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% lsr                            [50]
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% which lsr                      [51]
lsr: aliased to CLICOLOR_FORCE="yes" /bin/ls -lRGF "$@" |less -R
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% ls -lR                         [52]
total 0
drwxr-xr-x   9 AnneGoossens  staff  306 Nov 26 12:11 Days/
drwxr-xr-x  14 AnneGoossens  staff  476 Nov 26 12:12 Months/

./Days:
total 56
-rw-r--r--@ 1 AnneGoossens  staff   7 Nov 26 08:58 friday.txt
-rw-r--r--@ 1 AnneGoossens  staff   7 Nov 26 08:57 monday.txt
-rw-r--r--@ 1 AnneGoossens  staff   9 Nov 26 08:58 saturday.txt
-rw-r--r--@ 1 AnneGoossens  staff   7 Nov 26 08:58 sunday.txt
-rw-r--r--@ 1 AnneGoossens  staff   9 Nov 26 08:58 thursday.txt
-rw-r--r--@ 1 AnneGoossens  staff   8 Nov 26 08:57 tuesday.txt
-rw-r--r--@ 1 AnneGoossens  staff  10 Nov 26 08:57 wednesday.txt

./Months:
total 96
-rw-r--r--@ 1 AnneGoossens  staff  17 Nov 26 10:24 april.txt
-rw-r--r--@ 1 AnneGoossens  staff  18 Nov 26 10:25 august.txt
-rw-r--r--@ 1 AnneGoossens  staff  21 Nov 26 10:26 december.txt
-rw-r--r--@ 1 AnneGoossens  staff  20 Nov 26 10:24 february.txt
-rw-r--r--@ 1 AnneGoossens  staff  30 Nov 26 10:23 january.txt
-rw-r--r--@ 1 AnneGoossens  staff  16 Nov 26 10:25 july.txt
-rw-r--r--@ 1 AnneGoossens  staff  16 Nov 26 10:25 june.txt
-rw-r--r--@ 1 AnneGoossens  staff  17 Nov 26 10:24 march.txt
-rw-r--r--@ 1 AnneGoossens  staff  15 Nov 26 10:25 may.txt
-rw-r--r--@ 1 AnneGoossens  staff  21 Nov 26 10:26 november.txt
-rw-r--r--@ 1 AnneGoossens  staff  20 Nov 26 10:26 october.txt
-rw-r--r--@ 1 AnneGoossens  staff  21 Nov 26 10:26 september.txt
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% cat Months/*ember.txt          [53]
Month 12 is December
Month 11 is November
Month 9 is September
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% which cowsay                   [54]
cowsay not found
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% l                              [55]
total 0
drwxr-xr-x   9 AnneGoossens  staff   306B Nov 26 12:11 Days/
drwxr-xr-x  14 AnneGoossens  staff   476B Nov 26 12:12 Months/
[AnneGoossens@MacBook-Pro-van-Anne-Goossens: ~/Documents/Testfiles]% curl artez.nl                  [56]
<!DOCTYPE html>
<html>
    <head>

```



## Concept

```
Concept 1 = {

Doormiddel van web-scraping wordt er het laatste nieuws van het afgelopen uur van NU.nl afgehaald. 


'nieuws': 'www.nu.nl',
	

Woensdag 09 december 2015

Het laatste nieuws het eerst op NU.nl 
Temperatuur 6 °C 
Vervoer 0 Files 2 NS € 1,573 
AEX 440,85 

Het nieuws 
	•	￼ ￼ 1.  1 uur geleden Voor bij het nieuws Dit zijn de conclusies uit het onderzoek naar de Teeven-deal Dit zijn de belangrijkste conclusies uit het onderzoek van de commissie-Oosting naar de zogeheten 'Teeven-deal' uit 2000, die dit voorjaar leidde tot het aftreden van minister Ivo Opstelten en staatssecretaris Fred Teeven van Veiligheid en Justitie.  
	•	￼ ￼ 2.  1 uur geleden Voor bij het nieuws Reacties op kritisch onderzoek naar Teeven-deal De onderzoekscommissie-Oosting oordeelde woensdag hard over de zogenaamde Teeven-deal, tussen toenmalig officier van justitie Fred Teeven en drugscrimineel Cees H. in 2000. Dit zijn de reacties op het rapport.  
	•	￼ ￼ 3.  1 uur geleden Voor bij het nieuws Profiel Rabobank: Van boerenleenbanken naar marktleider hypotheken Rabobank schrapt de komende drie jaar nog eens negenduizend voltijdsbanen. Een profiel van het financiële concern. 
	
	
	

Concept 2 = {
￼Doormiddel van >>> raw_input() wordt er gevraagd naar je naam. In dit geval naar alle namen van de klas op volgorde van de GitHub lijst, en deze wordt vervolgens geprint.

Last login: Sun Jan  3 13:06:17 on ttys001
MacBook-Pro-van-Anne-Goossens:~ AnneGoossens$ python
Python 2.7.10 (default, Jul 14 2015, 19:46:27) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> raw_input()
print (raw_input('What is your name?'))
"print (raw_input('What is your name?'))"
>>> ('Anne')
'Anne'
>>> a = raw_input('What is your name?')
What is your name? Angela
>>> b = raw_input('What is your name?')
What is your name? Bas
>>> c = raw_input('What is your name?')
What is your name? Bella
>>> d = raw_input('What is your name?')
What is your name? Esmee
>>> e = raw_input('What is your name?')
What is your name? Floris
>>> f = raw_input('What is your name?')
What is your name? Heike
>>> g = raw_input('What is your name?')
What is your name? Ilse
>>> h = raw_input('What is your name?')
What is your name? Isabel
>>> i = raw_input('What is your name?')
What is your name? Jasmijn
>>> j = raw_input('What is your name?')
What is your name? Jeanine
>>> k = raw_input('What is your name?')
What is your name? Jesse
>>> l = raw_input('What is your name?')
What is your name? Kimberley
>>> m = raw_input('What is your name?')
What is your name? Leonie
>>> n = raw_input('What is your name?')
What is your name? Lola
>>> o = raw_input('What is your name?')
What is your name? Luc
>>> p = raw_input('What is your name?')
What is your name? Lydienne
>>> q = raw_input('What is your name?')
What is your name? Marianne
>>> r = raw_input('What is your name?')
What is your name? Marleen
>>> s = raw_input('What is your name?')
What is your name? Martijn
>>> t = raw_input('What is your name?')
What is your name? Max
>>> u = raw_input('What is your name?')
What is your name? Niels
>>> v = raw_input('What is your name?')
What is your name? Nikki
>>> w = raw_input('What is your name?')
What is your name? Nikki L
>>> x = raw_input('What is your name?')
What is your name? Noa
>>> y = raw_input('What is your name?')
What is your name? Patrick
>>> z = raw_input('What is your name?')
What is your name? Reinier
>>> print ('Anne' + a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z)
Anne Angela Bas Bella Esmee Floris Heike Ilse Isabel Jasmijn Jeanine Jesse Kimberley Leonie Lola Luc Lydienne Marianne Marleen Martijn Max Niels Nikki Nikki L Noa Patrick Reinier
>>> 

```

## Prototype: working demo

## Design the flow of the program

## How to use the script

## PDF format 
			
