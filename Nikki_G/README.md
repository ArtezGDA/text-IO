# Nikki G's work for Text IO 

## Homework
[collections]() (python code)

###Cowsay

```
Last login: Thu Dec  3 13:44:04 on ttys000
[Nikki@MacBook-Pro-van-Nikki: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
It appears Homebrew is already installed. If your intent is to reinstall you
should do the following before running this installer again:
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
The current contents of /usr/local are bin Cellar clamXav CODEOFCONDUCT.md CONTRIBUTING.md Library LICENSE.txt opt README.md share SUPPORTERS.md .git .gitignore
[Nikki@MacBook-Pro-van-Nikki: ~]% cowsay "Hoi"                             [73]
 _____ 
< Hoi >
 ----- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
[Nikki@MacBook-Pro-van-Nikki: ~]% cowsay -f stegosaurus "Hoi"              [74]
 _____ 
< Hoi >
 ----- 
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
[Nikki@MacBook-Pro-van-Nikki: ~]% 

```

### Array
```
a = ["Filosofie", "Fotografie", "Design Reaserch", "Annie", "Computer Skills", "Media Design", "Typografie", "Grafisch"]
print len(a)

a + ["Media Theorie"]

#a.append("Media Theorie")

print len (a)

a.pop(7)
print len (a)

a.pop(3)
print len (a)

print a[4]


print a
```

###Dictonairy
```
d = { 'adres':19, 'oppervlakte kamer': "21 m2", 'hoogte kamer': "3,2 m", 'bedgrootte': "2persoons 160cm bij 200 cm", 'merk printer': "Epson XP-950"}

print 'adres'    
```


### Poe
```
"Last login: Wed Dec  2 13:22:37 on ttys000[Nikki@MacBook-Pro-van-Nikki: ~]% cd Documents/A\ School/Artez\ GD2A/Media\ Design/Huiswerk\ 3\ dec [Nikki@MacBook-Pro-van-Nikki: ~]% curl http://www.gutenberg.org/files/2147/2147-8.txt > vol1.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   313k      0  0:00:01  0:00:01 --:--:--  
[Nikki@MacBook-Pro-van-Nikki: ~]% curl http://www.gutenberg.org/files/2148/2148-8.txt > vol2.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   313k      0  0:00:01  0:00:01 --:--:--  313k 313k
[Nikki@MacBook-Pro-van-Nikki: ~]% curl http://www.gutenberg.org/files/2149/2149-8.txt > vol3.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   313k      0  0:00:01  0:00:01 --:--:--  313k
[Nikki@MacBook-Pro-van-Nikki: ~]% curl http://www.gutenberg.org/files/2147/2147-8.txt > vol4.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   313k      0  0:00:01  0:00:01 --:--:--  313k
[Nikki@MacBook-Pro-van-Nikki: ~]% curl http://www.gutenberg.org/files/2147/2147-8.txt > vol5.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   313k      0  0:00:01  0:00:01 --:--:--  313k[Nikki@MacBook-Pro-van-Nikki: Artez GD2A/Media Design/Huiswerk 3 dec]% mkdir Poe[Nikki@MacBook-Pro-van-Nikki: Artez GD2A/Media Design/Huiswerk 3 dec]% mv .txt Poemv: rename .txt to Poe/.txt: No such file or directory[Nikki@MacBook-Pro-van-Nikki: Artez GD2A/Media Design/Huiswerk 3 dec]% mv *.txt Poe[Nikki@MacBook-Pro-van-Nikki: Artez GD2A/Media Design/Huiswerk 3 dec]% l   [60]total 0drwxr-xr-x  7 Nikki  staff   238B Dec  2 13:30 Poe/[Nikki@MacBook-Pro-van-Nikki: Artez GD2A/Media Design/Huiswerk 3 dec]% cd Poe [Nikki@MacBook-Pro-van-Nikki: Media Design/Huiswerk 3 dec/Poe]% grep -c 'dog' .txtegrep: .txt: No such file or directory[Nikki@MacBook-Pro-van-Nikki: Media Design/Huiswerk 3 dec/Poe]% grep -c 'dog' *.txtvol1.txt:10vol2.txt:17vol3.txt:19vol4.txt:25vol5.txt:13[Nikki@MacBook-Pro-van-Nikki: Media Design/Huiswerk 3 dec/Poe]% grep -c 'cat' *.txtvol1.txt:132vol2.txt:134vol3.txt:79vol4.txt:110vol5.txt:74[Nikki@MacBook-Pro-van-Nikki: Media Design/Huiswerk 3 dec/Poe]% grep -n 'horror' *.txtvol1.txt:591:subtle ramifications of its roots. In raising images of horror, also,\vol1.txt:593:some terrible _doubt _which is the secret of all horror. He leaves to\vol1.txt:617:the unreal as sources of effect. They have not used dread and horror\vol1.txt:1375:any adequate idea of the horror of my situation. I gasped convulsively\vol1.txt:1400:nor horror-stricken. If I felt any emotion at all, it was a kind of\vol1.txt:1445:die rapidly away, and thereunto succeeded horror, and dismay, and a\vol1.txt:2341:can give any adequate idea of the extreme, the absolute horror and\vol1.txt:5011:every one present not less with horror than with astonishment.\vol1.txt:5335:horror of the thing. But dismiss the idle opinions of this print. It\vol1.txt:5673:brutal, a butchery without motive, a _grotesquerie_ in horror absolutely\vol1.txt:5728:to all. I understood the full horrors of the murder at once.\vol1.txt:5942:fell from his hold through excess of horror. Now it was that those\vol1.txt:5967:horror, was just discernible. The fury of the beast, who no doubt bore\vol1.txt:5982:Frenchman's exclamations of horror and affright, commingled with the\vol1.txt:7604:in fact, a secret. The horrors of this dark deed are known only to one,\vol1.txt:7701:unutterable horror at finding that the boat has been picked up and\vol1.txt:8483:attended us. All around were horror, and thick gloom, and a black\vol1.txt:8521:mainly inspired us with horror and astonishment, was that she bore up\vol1.txt:8719:To conceive the horror of my sensations is, I presume, utterly\vol1.txt:8736:horror upon horror! the ice opens suddenly to the right, and to the\vol2.txt:1543:of the magnificence, or of the horror of the scene--or of the wild\vol2.txt:1744:horror--for he put his mouth close to my ear, and screamed out the word\vol2.txt:1801:the place at all. As it was, I involuntarily closed my eyes in horror.\vol2.txt:1883:"Never shall I forget the sensations of awe, horror, and admiration with\vol2.txt:2023:removed) speechless from the memory of its horror. Those who drew me on\vol2.txt:2979:then present had been unaccustomed to death-bed horrors; but so hideous\vol2.txt:3015:unutterable, shuddering horror which these few words, thus uttered, were\vol2.txt:3181:the night's debauch--I experienced a sentiment half of horror, half of\vol2.txt:3317:and horror with which the animal inspired me, had been heightened by one\vol2.txt:3446:howl--a wailing shriek, half of horror and half of triumph, such as\vol2.txt:3664:instruments, which did not inspire him with horror.\vol2.txt:3913:horror, we partially turned aside the yet unscrewed lid of the coffin,\vol2.txt:3963:intense sentiment of horror, unaccountable yet unendurable, I threw on\vol2.txt:4292:redness and the horror of blood. There were sharp pains, and sudden\vol2.txt:4432:surprise--then, finally, of terror, of horror, and of disgust.\vol2.txt:4451:was besprinkled with the scarlet horror.\vol2.txt:4496:horror at finding the grave-cerements and corpse-like mask which they\vol2.txt:4949:horror become merged in a cloud of unnamable feeling. By gradations,\vol2.txt:4956:delight of its horror. It is merely the idea of what would be our\vol2.txt:5722:delirious horror, the soft and nearly imperceptible waving of the sable\vol2.txt:5772:interminableness of the descent. They tell also of a vague horror at\vol2.txt:5833:thronging upon my recollection a thousand vague rumors of the horrors of\vol2.txt:5909:or death with its most hideous moral horrors. I had been reserved for\vol2.txt:5973:my side on the floor. I saw, to my horror, that the pitcher had been\vol2.txt:5974:removed. I say to my horror; for I was consumed with intolerable thirst.\vol2.txt:6004:idea that had perceptibly descended. I now observed--with what horror it\vol2.txt:6014:agents--the pit whose horrors had been destined for so bold a recusant\vol2.txt:6024:What boots it to tell of the long, long hours of horror more than\vol2.txt:6164:my wooden bed of horror upon the stone floor of the prison, when the\vol2.txt:6196:A richer tint of crimson diffused itself over the pictured horrors of\vol2.txt:6206:reason.--Oh! for a voice to speak!--oh! horror!--oh! any horror but\vol2.txt:6407:no sooner was he awake than he became fully aware of the awful horrors\vol2.txt:6490:which still palpitates, a degree of appalling and intolerable horror\vol2.txt:6558:the grim Darkness overspread the Earth, then, with every horror of\vol2.txt:6615:unstrung, and I fell a prey to perpetual horror. I hesitated to ride, or\vol2.txt:7785:been already too much an object for the scorn--for the horror--for the\vol2.txt:7812:am I not now dying a victim to the horror and the mystery of the wildest\vol2.txt:8156:possessed with an objectless yet intolerable horror. Gasping for\vol2.txt:8354:I say that I felt all the horrors of the damned? Most assuredly I had\vol2.txt:8400:from Oxford to the continent, in a perfect agony of horror and of shame.\vol2.txt:8499:astonishment, that horror which possessed me at the spectacle then\vol2.txt:8706:horror!-this I thought, and this I think. But anything was better than\vol2.txt:8966:dreams a cry as of horror and dismay; and thereunto, after a pause,\vol2.txt:8982:comprehension. Yet its memory was replete with horror--horror more\vol2.txt:9160:involved a penalty the exceeding great horror of which will not permit\vol3.txt:754:description. Every species of calamity and horror befell me. Among other\vol3.txt:905:My sensations were those of extreme horror and dismay. In vain I\vol3.txt:1094:horror with which I was inspired by the fragmentary warning thus\vol3.txt:1120:horrors which encompassed me. For another twenty-four hours it was\vol3.txt:1461:What was his grief and horror in discovering that the latter had\vol3.txt:2383:visitation, and that the appalling horror which has sometimes been\vol3.txt:2386:anticipative horror, lest the apparition might possibly be real, than\vol3.txt:2416:pitiable objects of horror and utter despair my eyes ever encountered.\vol3.txt:2613:us more fully the horrors which surrounded us. The brig was a mere\vol3.txt:2833:extremes first of delight and then of horror, than even any of the\vol3.txt:2907:of her decks. Shall I ever forget the triple horror of that spectacle?\vol3.txt:2915:raving with horror and despair--thoroughly mad through the anguish of\vol3.txt:3091:indescribable state of weakness and horror, brought on by the wine,\vol3.txt:3331:the tumultuous dangers of the storm or the gradually approaching horrors\vol3.txt:3384:horror of their reality. Let it suffice to say that, having in some\vol3.txt:3686:horror at the sound.\vol3.txt:5343:horror not to be tolerated--never to be conceived.\vol3.txt:5659:expressions of mingled horror, rage, and intense curiosity depicted\vol3.txt:5921:all imagined horrors crowding upon me in fact. I felt my knees strike\vol3.txt:5926:the cliff; and, with a wild, indefinable emotion, half of horror, half\vol4.txt:824:box with a blindfold impetuosity--but who shall describe his horror when\vol4.txt:1075:to the wall. To his extreme horror and astonishment, the head of the\vol4.txt:1237:recoil in horror from the deep and impressive meaning of his terrible\vol4.txt:1308:haste in the first place, and, in the second, a very usual horror at the\vol4.txt:2010:emotions of wonder and horror with which I gazed, when, leaping\vol4.txt:2630:my head gently to one side, I perceived, to my extreme horror, that the\vol4.txt:2683:But now a new horror presented itself, and one indeed sufficient to\vol4.txt:5012:insignificance, when to my extreme horror and astonishment I discovered\vol4.txt:5229:the belligerents, and throwing open the sash to their extreme horror and\vol4.txt:7744:terror, of horror, or of wo. You alone, habited in a white robe, passed\vol4.txt:8046:general lamentation and horror. This first sense of pain lay in a\vol4.txt:8067:details, of the fiery and horror-inspiring denunciations of the\vol4.txt:8174:And then did we, the seven, start from our seats in horror, and stand\vol5.txt:620:on its breast, with a feeling or horror and awe--with a sentiment of\vol5.txt:1065:shrieks of the multitude who gazed at them from below, horror-stricken,\vol5.txt:1107:takes up a burthen so heavy in horror that it can be thrown down only\vol5.txt:1882:seem to be rendered torpid, so that they have a horror of any thing like\vol5.txt:2243:room fainted outright through sheer horror. But after the first wild,\vol5.txt:4449:     And thy Angel I'll be, 'mid the horrors of this,--\vol5.txt:5260:             What a horror they outpour\vol5.txt:6931:  With horror and awe!\[Nikki@MacBook-Pro-van-Nikki: Media Design/Huiswerk 3 dec/Poe]%            [72]```
###Itunes
```
Itunens = {
	'Caracal (Deluxe)': [
	{ 
		'artist': "Disclosure",
		'year':2015, 
		'songs': [
		{'title1': 'nocturnal', 'time': 6.44},
		{'title2': 'omen', 'time': 3.50},
		{'title3': 'holding on', 'time': 5.15},
		{'title4': 'willing & able', 'time': 4.52},
		{'title5': 'magnets', 'time': 3.19},
		{'title6': 'jaded', 'time': 4.33},
		{'title7': 'good itentions', 'time': 4.42},
		{'title8': 'superego', 'time': 4.33},
		{'title9': 'hourglass', 'time': 5.24},
		{'title10': 'echoes', 'time': 5.09},
		{'title11': 'masterpiece', 'time': 4.01},
		{'title12': 'molecules', 'time': 3.56},
		{'title13': 'moving mountains', 'time': 5.35},
		{'title14': 'bang that', 'time': 4.48},
		{'title15': 'afterthought', 'time': 5.20},
		]
	},

	
	],
}```
### Kamer
```
kamer = {
	'kamer': [
	{
		'plaats': "Arnhem", 
		'straat naam': 'Kastanjelaan 17' , 
		'postcode': '6828 GH',
		'huisnummer':17,
	},

	{
		'opp':21 ,
		'hoogte':3.10 , 
		'lengte':3.50 , 
		'breedte':6, 
	},

	{
		'interieur': [
			{'banken':0 },
			{'bureaus': 1 },
			{'kasten': 1},
			{'deur': 2 },
			{'ramen': 2},
			]
	},
	
	],

	}```
###Groeps datastructure
```

typeface = {
    
"kapitaal":
    [
        {
           
   "letters": [
       { 
            'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,': [
                    {
                        "A": [
                            {
                                "compartmenten":[{
                                    "1":[{'coordinaten hoekpunten':[{
                                        "coordinaten hoekpunt 1":[15.25,9.74],
                                        "coordinaten hoekpunt 1":[15.25,9.74],
                                        "coordinaten hoekpunt 1":[15.06 , 9.81],
                                        "coordinaten hoekpunt 1":[14.94 , 9.74],
                                        "coordinaten hoekpunt 1":[15.80 , 10.12],
                                        "coordinaten hoekpunt 1":[15.15 , 10.16],
                                        "coordinaten hoekpunt 1":[15.20 , 10.08],
                                        "coordinaten hoekpunt 1":[15.61 , 10.08],
                                        "coordinaten hoekpunt 1":[15.61 , 9.93],
                                        "coordinaten hoekpunt 1":[15.61 , 10.31],
                                        "coordinaten hoekpunt 1":[15.61 , 10.16],
                                        }],
                                        
                                        
                                    }],
                                 
                                }],
                            
                                "tussen ruimte":[{
                                    "AE":[0.9],
                                    
                                  
                                }],
                              "kleur":['zwart'],
                               }],
                              }],
                            }],
                          }],
                                
                      "kerning":[{
                            'M,N,O,R,P,G,L':[{ 
                                'L':[{
                                        'hoekpunt':[15.13 , 10.63 ],
                                        'hoekpunt':[15.32 , 10.44 ],
                                        'hoekpunt':[15.09 , 10.17],
                                        'hoekpunt':[15.17 , 10.17 ],
                                        'hoekpunt':[15.18 , 9.96 ],
                                        'hoekpunt':[15.24 , 10.01],
                                        'hoekpunt':[15.40 , 9.94],
                                        'hoekpunt':[15.40 , 9.87],
                                        'hoekpunt':[15.61 , 9.96 ],
                                        'hoekpunt':[14.94 , 10.44],
                                        'hoekpunt':[15.09 , 10.44],
                                        'hoekpunt':[15.70 , 10.44],
                                        "tussen ruimte":[{
                                        "AE":[0.9],
                                    
                                }],
                              "kleur":['zwart'],
                               
                                }],
                            }],
                        }],
                    
"onderkasten":
        [{
                
        "letters": [{
            
              'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z': [{
                  
                   "acde": [{
                       
                        "a": [{
                            
                           "compartement":[{'coordinaten hoekpunten buitenvorm':[{
                                    'hoekpunt':[14.44 , 10.35],
                                    'hoekpunt':[14.88 , 10.35],
                                    'hoekpunt':[14.88 , 10.17],
                                    'hoekpunt':[15.17 , 10.17 ],
                                    'hoekpunt':[15.18 , 9.96 ],
                                    'hoekpunt':[15.24 , 10.01],
                                    'hoekpunt':[15.40 , 9.94],
                                    'hoekpunt':[15.40 , 9.87],
                                    'hoekpunt':[15.61 , 9.96 ],
                                    'hoekpunt':[14.94 , 10.44],
                                    'hoekpunt':[15.09 , 10.44],
                                    'hoekpunt':[15.70 , 10.44],
                                }]
                                }],
                             "compartement binnenvorm":[{
                                     'hoekpunt':[14.54 , 10.40],
                                     'hoekpunt':[14.98 , 10.40],
                                     'hoekpunt':[14.98 , 10.30],
                                     'hoekpunt':[15.19 , 10.50],
                                     'hoekpunt':[14.98 , 10.70],
                                     'hoekpunt':[14.98 , 10.60],
                                     'hoekpunt':[14.54 , 10.60],
                                 }],
                                 }],
                              "tussen ruimte":[{
                                  "ha":['1'],
                              }],
                              }],
                              }],
                            
                    
                   "fghijklm": [{
                       
                        "f": [{
                            
                           "compartement":[{'coordinaten hoekpunten buitenvorm compartement':[{
                                     'hoekpunt':[103  , 143],
                                     'hoekpunt':[104  , 143],
                                     'hoekpunt':[102  , 144],
                                     'hoekpunt':[108  , 144],
                                     'hoekpunt':[108  , 145],
                                     'hoekpunt':[102  , 145],
                                     'hoekpunt':[104  , 146],
                                     'hoekpunt':[103  , 147],
                                     'hoekpunt':[103  , 147],
                                     'hoekpunt':[101  , 145],
                             }],
                             }],
                              
                              "tussen ruimte":[{"fa":[1,8],
                             }],
                             }],
                             }],
                   
                    "p,q,t,u": [{
                        
                        "p": [{
                            
                           "compartement":[{'coordinaten hoekpunten':[{  
                                 'hoekpunt':[103  , 143],
                                 'hoekpunt':[104  , 138],
                                 'hoekpunt':[108  , 146],
                                 'hoekpunt':[99  , 146],
                             }],}],}],
                             
                              "tussen ruimte":[{"pa":[1,8],
                             }], 
                             }],
                             }],
             
                    "r,s,v,w,x,y,z": [{
                        
                        "r": [{
                            
                           "compartement":[{'coordinaten hoekpunten':[{
                                 'hoekpunt':[105  , 145],
                                 'hoekpunt':[109  , 152],
                                 'hoekpunt':[100  , 152],
                             }],
                             }],
                            
                           "compartement binnenvorm":[{  
                                 'hoekpunt':[105  , 149],
                                 'hoekpunt':[108  , 152],
                                 'hoekpunt':[101  , 152],
                               
                             }],
                             }],
                             
                              "tussen ruimte":[{
                                  "ra":[1,8],
                             }],          
                             }],
                             }],

'leestekens':[{".,?!@ $%^&#*-(_=+[]{}:;\|<>/`~)	~":
            
        [{
                    "compartement":[{'coordinaten hoekpunten':
        [{
                             'hoekpunt':[ 104.931,146.037],
                             'hoekpunt':[ 108.754,149.860],
                             'hoekpunt':[101.118, 152],
                             'hoekpunt':[105 , 148.865],
        }],
        }],
                    "tussen ruimte":[{",?":[1.65],}],
        }],
        }],
    
'cijfers':[{'1,2,3,4,5,6,7,8,9,0,':
        [{ '3':[{   "compartement 1":[{'coordinaten hoekpunten':
        [{ 
                            'hoekpunt':[ 14.47 , 10.50],
                            'hoekpunt':[14.66 , 10.31 ],
                            'hoekpunt':[14.77 , 10.46],
                            'hoekpunt':[14.77 , 10.54],
                            'hoekpunt':[14.66 , 10.54],
                            'hoekpunt':[14.66 , 10.69], 
        }],
                    "compartement 2":[{'coordinaten hoekpunten':[{'coordinaten hoekpunten':[{ 
                            'hoekpunt':[14.82 , 10.82],
                            'hoekpunt':[14.93 , 10.46],
                            'hoekpunt':[14.77 , 10.54],
                            'hoekpunt':[14.82 , 10.54],
        }],
        }],
                    "compartement 3":[{'coordinaten hoekpunten':[{ 
                            'hoekpunt':[14.98 , 10.46],
                            'hoekpunt':[15.08 , 10.46 ],
                            'hoekpunt':[15.08 , 10.54],
                            'hoekpunt':[ 14.98 , 10.54],
        }],
        }],
                    "compartement 4":[{'coordinaten hoekpunten':[{ 
                            'hoekpunt':[15.13 , 10.46],
                            'hoekpunt':[15.23 , 10.46  ],
                            'hoekpunt':[15.23 , 10.54],
                            'hoekpunt':[14.13 , 10.54],
        }]
        }],
        }],
        }],
        
                    "tussen ruimte":[{"34":[1],}],
        }],
        }],
        }],
        }

```


## Concept

Mijn idee was om tekst als een emotie in te voeren, en vervolgens dat er een digitale smiley uitkomt. Als een computer die tie toch emoties kan tonen. Dit moet alleen nog verder ontwikkeld worden. 


## Prototype: working demo

```
emoties = { 
	'emoties' :[
	{
		'boos': " >:( ",
		'blij': " :) ",
		'verdrietig': " :'(",
		'verbaasd': " :o",
		'heel blij': " :D",
		'knipoog': " ;)",
		'vragend': " :/ ",
		'tevreden': " ^^ ",
		'beertje blij': " :3 "

	}],}

```

## Design the flow of the program

## How to use the script

## PDF format 
			
