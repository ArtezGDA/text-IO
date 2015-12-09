**Search files**

```
Last login: Wed Dec  2 19:18:21 on console
a-cwp-04:~ h.dewit$ /Volumes/h.dewit/Documents/Testfiles/Months 
-bash: /Volumes/h.dewit/Documents/Testfiles/Months: is a directory
a-cwp-04:~ h.dewit$ cd /Volumes/h.dewit/Documents/Testfiles/Months
a-cwp-04:Months h.dewit$ ls *ember.txt
december.txt	november.txt	september.txt

```
**Downloading Edgar Allan Poe documents**

```
[h.dewit@a-les1-08: ~]% pwd                                                 [2]
/Users/h.dewit
[h.dewit@a-les1-08: ~]% mkdir ~/Documents/Poe                               [3]
[h.dewit@a-les1-08: ~]% cd ~/Documents/Poe                                  [3]
[h.dewit@a-les1-08: ~/Documents/Poe]% curl http://www.gutenberg.org/files/2147/2147-8.txt > vol1.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  537k  100  537k    0     0   429k      0  0:00:01  0:00:01 --:--:--  429k
[h.dewit@a-les1-08: ~/Documents/Poe]% curl http://www.gutenberg.org/files/2148/2148-8.txt > vol2.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  566k  100  566k    0     0   354k      0  0:00:01  0:00:01 --:--:--  354k
[h.dewit@a-les1-08: ~/Documents/Poe]% curl http://www.gutenberg.org/files/2149/2149-8.txt > vol3.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  582k  100  582k    0     0   427k      0  0:00:01  0:00:01 --:--:--  427k
[h.dewit@a-les1-08: ~/Documents/Poe]% curl http://www.gutenberg.org/files/2150/2150-8.txt > vol4.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  475k  100  475k    0     0   364k      0  0:00:01  0:00:01 --:--:--  365k
[h.dewit@a-les1-08: ~/Documents/Poe]% curl http://www.gutenberg.org/files/2151/2151-8.txt > vol5.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  463k  100  463k    0     0   436k      0  0:00:01  0:00:01 --:--:--  436k

```
**Counting 'cat'**

```
[h.dewit@a-les1-08: ~/Documents/Poe]% ls                                    [9]
vol1.txt  vol2.txt  vol3.txt  vol4.txt  vol5.txt
[h.dewit@a-les1-08: ~/Documents/Poe]% grep -c -i 'cat' vol*.txt            [10]
vol1.txt:133
vol2.txt:138
vol3.txt:114
vol4.txt:116
vol5.txt:80

```
**Everytime 'cat' is mentioned**

```
[h.dewit@a-les1-08: ~/Documents/Poe]% grep -i 'cat' vol*.txt               [11]
vol1.txt:of conscience as "William Wilson," "The Black Cat" and "The Tell-tale
vol1.txt:though none of the usual signs of intoxication were visible, his will
vol1.txt:warmth to her by chafing her hands and her feet, while her pet cat was
vol1.txt:from William Winter's poem, read at the dedication exercises of the
vol1.txt:Having received a classical education in England, he returned home and
vol1.txt:nature, and a delicate appreciation of classic models, but give no hint
vol1.txt:to have had an educated taste, we should have had a series of poems from
vol1.txt:combinations of words, a capacity wholly dependent on a delicate
vol1.txt:all the miracles of smooth juvenile versification. A school-boy, one
vol1.txt:subtle ramifications of its roots. In raising images of horror, also,
vol1.txt:and in the subtle metaphysical analysis of both, indications of the
vol1.txt:usual signs of intoxication were visible, his will was palpably insane.
vol1.txt:phase of his character. Under that degree of intoxication which only
vol1.txt:character. His letters, of which the constant application for autographs
vol1.txt:serious, communications.
vol1.txt:the writer of this communication, am the identical Hans Pfaall himself.
vol1.txt:The limited nature of my education in general, and more especially my
vol1.txt:barometer with some important modifications, and two astronomical
vol1.txt:Nantz, in France, by whom it was conditionally communicated to myself.
vol1.txt:the car a pair of pigeons and a cat. It was now nearly daybreak, and I
vol1.txt:extricating myself from this dilemma; and I never, for a moment, looked
vol1.txt:From indications afforded by the barometer, we find that, in ascensions
vol1.txt:the most delicate means we possess of ascertaining the presence of the
vol1.txt:life is and must be essentially incapable of modification at any given
vol1.txt:successful application, if I could manage to complete the voyage within
vol1.txt:feeling no pain whatever in the head. The cat was lying very demurely
vol1.txt:escape, were busily employed in picking up some grains of rice scattered
vol1.txt:however, breathing with tolerable freedom. The cat and pigeons seemed to
vol1.txt:"I was now rising rapidly, and by seven o'clock the barometer indicated
vol1.txt:a measure, ceased, I could catch my breath only at long intervals, and
vol1.txt:in the extreme, and struggled to escape; while the cat mewed piteously,
vol1.txt:use of my condenser. In the meantime, looking toward the cat, who was
vol1.txt:of the mighty cataract. Overhead, the sky was of a jetty black, and the
vol1.txt:and cat entirely with a barricade against the highly rarefied atmosphere
vol1.txt:vacuum at any moment within the chamber, this purification was never
vol1.txt:atmosphere ejected. For the sake of experiment I had put the cat and
vol1.txt:was one of an extended construction. It then indicated an altitude on
vol1.txt:within the chamber, I took that opportunity of observing the cat and
vol1.txt:kittens through the valve. The cat herself appeared to suffer again very
vol1.txt:family of cats, and deprived me of the insight into this matter which a
vol1.txt:either cat or kittens would ever live to tell the tale of their
vol1.txt:indicating my various altitudes, respectively, at different periods,
vol1.txt:qualification, may be called the limit of human discovery in these
vol1.txt:diminished not at all, and I could discover no indication whatever of a
vol1.txt:communicate. I have much to say of the climate of the planet; of its
vol1.txt:for speech in a singular method of inter-communication; of the
vol1.txt:farther communication on my part--in consideration of the light which
vol1.txt:publication of the hoax.
vol1.txt:as regards an attempt at _verisimilitude, _in the application of
vol1.txt:(*3) Since the original publication of Hans Pfaall, I find that Mr.
vol1.txt:mortification consequent upon his disasters, he left New Orleans, the
vol1.txt:to excite interest and esteem. I found him well educated, with unusual
vol1.txt:I felt it, and, to say the truth, found not the slightest indication of
vol1.txt:you!--answer me this instant, without prevarication!--which--which is
vol1.txt:his right eye that the negro indicated.
vol1.txt:certain indications of method, removed the peg which marked the spot
vol1.txt:in a straight line to the distance of fifty feet, a spot was indicated,
vol1.txt:identification. Besides all this, there was a vast quantity of solid
vol1.txt:re-application of heat.
vol1.txt:loss of a memorandum indicating its locality--had deprived him of the
vol1.txt:not, by proper application, resolve. In fact, having once established
vol1.txt:repetitions of any three characters, in the same order of collocation,
vol1.txt:clearly indicated by the words, 'northeast and by north.' This latter
vol1.txt:thence extended to a distance of fifty feet, would indicate a definite
vol1.txt:way, by a little bit of sober mystification. For this reason I swung
vol1.txt:time, the advantages of a modern education. Therefore cease to regard
vol1.txt:domesticated in the city. A mutiny has been the result; and, as is usual
vol1.txt:in danger of mastication! Therefore never regard so piteously thy tail;
vol1.txt:an arrow from a catapult he approaches the hippodrome! He leaps!--he
vol1.txt:departure!--for we shall find our delicate modern ears unable to endure
vol1.txt:perception, indications of the true state of affairs. The first two
vol1.txt:guesser and a persevering man. But, without educated thought, he erred
vol1.txt:panel in the window, indicating a _loge de concierge._ Before going in
vol1.txt:implicated in their perpetration. Of the worst portion of the crimes
vol1.txt:cat. The impossibility of egress, by means already stated, being thus
vol1.txt:utterance no syllabification could be detected."
vol1.txt:class of thinkers who have been educated to know nothing of the theory
vol1.txt:"Turn, now, to other indications of the employment of a vigor most
vol1.txt:syllabification. What result, then, has ensued? What impression have I
vol1.txt:the coherence of syllabification. Besides, the hair of a madman is not
vol1.txt:be impossible to prove me cognizant of the murder, or to implicate me
vol1.txt:although somewhat Neufchatelish, were still sufficiently indicative of a
vol1.txt:The sailor's face flushed up as if he were struggling with suffocation.
vol1.txt:measure implicated in them. From what I have already said, you must know
vol1.txt:assassin," or, if more than one should prove to have been implicated,
vol1.txt:implicate the parties suspected; and they were discharged forthwith.
vol1.txt:my notes, "that this is a far more intricate case than that of the
vol1.txt:each assumed, should have been understood as indicative rather of the
vol1.txt:them all in the same category. I have shown how it is that the body of
vol1.txt:identification of the corpse by Beauvais. In regard to the hair upon the
vol1.txt:idiot, could never have urged, in identification of the corpse, simply
vol1.txt:Affidavits of this character are readily made matter of mystification.
vol1.txt:"We have received one or two communications, the object of which is to
vol1.txt:"We have received several forcibly written communications, apparently
vol1.txt:that an elopement has again taken place) as indicating a renewal of the
vol1.txt:was supposed to indicate the precise scene of the outrage, it must be
vol1.txt:communications sent to the evening paper. These communications, although
vol1.txt:these communications, or of the public attention by them directed, the
vol1.txt:prior to the date of the communications by the guilty authors of these
vol1.txt:communications themselves.
vol1.txt:upper stone lay a white petticoat; on the second a silk scarf; scattered
vol1.txt:communications to the journals are much in the way of corroboration. The
vol1.txt:compare with each other the various communications sent to the evening
vol1.txt:compare these communications, both as regards style and MS., with
vol1.txt:compare these various communications with the known MSS. of the officer.
vol1.txt:insult him in imagining a possible necessity for modification. In their
vol1.txt:inappreciable, produces, at length, by dint of multiplication at all
vol1.txt:(*1) Upon the original publication of "Marie Roget," the foot-notes now
vol1.txt:different periods, long subsequent to the publication, confirmed, in
vol1.txt:into which a blind devotion to principles of classification has led the
vol1.txt:application to practice. He exhibited a model of his invention at the
vol1.txt:great rapidity, communicating a progressive motion to the whole. By
vol1.txt:generally supposed that some exceedingly complicated application must be
vol1.txt:objects, will always indicate the _course_. In the same way, the angle
vol1.txt:formed by the rope with the vertical axis of the machine, indicates
vol1.txt:about ten minutes after starting, the barometer indicated an altitude
vol1.txt:communicated, however, by Mr. Ainsworth to Mr. Forsyth. It was nearly
vol1.txt:other. Hereditary wealth afforded me an education of no common order,
vol1.txt:However, as the captain said he could perceive no indication of danger,
vol1.txt:scattered mathematical instruments of the most quaint and obsolete
vol1.txt:headlong dashing of a cataract.
vol1.txt:the maps of Mercator, in which the ocean is represented as rushing, by
vol1.txt:electronic work, you indicate that you have read, understand, agree to
vol1.txt:located in the United States, we do not claim a right to prevent you from
vol1.txt:1.D.  The copyright laws of the place where you are located also govern
vol1.txt:from the public domain (does not contain a notice indicating that it is
vol1.txt:work, (b) alteration, modification, or additions or deletions to any
vol1.txt:501(c)(3) educational corporation organized under the laws of the
vol1.txt:Revenue Service.  The Foundation's EIN or federal tax identification
vol1.txt:The Foundation's principal office is located at 4557 Melan Dr. S.
vol1.txt:Fairbanks, AK, 99712., but its volunteers and employees are scattered
vol1.txt:throughout numerous locations.  Its business office is located at
vol1.txt:with these requirements.  We do not solicit donations in locations
vol2.txt:     The Black Cat
vol2.txt:"It is merely," I said, "an identification of the reasoner's intellect
vol2.txt:effected the thorough identification in which his success consisted, I
vol2.txt:"And the identification," I said, "of the reasoner's intellect with that
vol2.txt:identification, and, secondly, by ill-admeasurement, or rather through
vol2.txt:square inches--what is it all but an exaggeration of the application of
vol2.txt:'analysis' into application to algebra. The French are the originators
vol2.txt:see that the most intricate and remote recess of his hotel would be
vol2.txt:but in all kinds of climbing, as Catalani said of singing, it is far
vol2.txt:black cat, I think) which she was narrating (all in an undertone, of
vol2.txt:cat (a black cat, I think it was) and the rat.
vol2.txt:the finishing stroke to the black cat and the rat (the rat was blue)
vol2.txt:"Isitsoornot," expressed no very particular intensity of gratification;
vol2.txt:things upon its back were vermin, such as sometimes infest cats and
vol2.txt:of little things like caterpillars'" (*1)
vol2.txt:"'Among the magicians, were domesticated several animals of very
vol2.txt:cats and dogs have any difficulty in seeing objects that do not exist at
vol2.txt:roar, such as not even the mighty cataract of Niagara ever lifts up in
vol2.txt:and most dreadful cataracts; the noise being heard several leagues off,
vol2.txt:water so that it precipitates itself like a cataract; and thus the
vol2.txt:precise location. Besides, if Mr. Kissam actually did come upon the
vol2.txt:paragraph in the 'Courier and Enquirer' a fabrication got up to 'make
vol2.txt:well authenticated, that we may receive it implicitly.
vol2.txt:furnace, with a glowing fire in it, and on the fire a kind of duplicate
vol2.txt:from the application of mustard to the nervous centres, but to-night
vol2.txt:a catechism."
vol2.txt:_P._ But in all this--in this identification of mere matter with God--is
vol2.txt:communicate similar ones to the optic nerve. The nerve conveys similar
vol2.txt:mind of the rudimental life communicates with the external world; and
vol2.txt:comparatively recent date. The ossification had proceeded with very
vol2.txt:(scarcely noticeable, unless through the application of a mirror to the
vol2.txt:distinct--syllabification. M. Valdemar spoke--obviously in reply to the
vol2.txt:make it follow the direction of my hand. The only real indication,
vol2.txt:The first indication of revival was afforded by a partial descent of the
vol2.txt:THE BLACK CAT.
vol2.txt:intensity of the gratification thus derivable. There is something in the
vol2.txt:had birds, gold-fish, a fine dog, rabbits, a small monkey, and _a cat_.
vol2.txt:black cats as witches in disguise. Not that she was ever _serious_ upon
vol2.txt:Pluto--this was the cat's name--was my favorite pet and playmate. I
vol2.txt:One night, returning home, much intoxicated, from one of my haunts about
vol2.txt:town, I fancied that the cat avoided my presence. I seized him; when, in
vol2.txt:In the meantime the cat slowly recovered. The socket of the lost eye
vol2.txt:white surface, the figure of a gigantic _cat_. The impression was given
vol2.txt:came to my aid. The cat, I remembered, had been hung in a garden
vol2.txt:myself of the phantasm of the cat; and, during this period, there came
vol2.txt:a black cat--a very large one--fully as large as Pluto, and closely
vol2.txt:any portion of his body; but this cat had a large, although indefinite
vol2.txt:the house it domesticated itself at once, and became immediately a great
vol2.txt:With my aversion to this cat, however, its partiality for myself seemed
vol2.txt:of the old building which our poverty compelled us to inhabit. The cat
vol2.txt:this indication of extensive decay, however, the fabric gave little
vol2.txt:through many dark and intricate passages in my progress to the _studio_
vol2.txt:lay scattered about, but failed to give any vitality to the scene. I
vol2.txt:delicate Hebrew model, but with a breadth of nostril unusual in similar
vol2.txt:and frequent although transient affections of a partially cataleptical
vol2.txt:amplification of the wild air of the last waltz of Von Weber. From the
vol2.txt:had been here, he imagined, fulfilled in the method of collocation of
vol2.txt:arrangement, and in its reduplication in the still waters of the tarn.
vol2.txt:cataleptical character, the mockery of a faint blush upon the bosom and
vol2.txt:roll, a cataract, over the fiery wall of the horizon. But there is no
vol2.txt:the profusion of golden ornaments that lay scattered to and fro or
vol2.txt:descent, and stood together on the damp ground of the catacombs of the
vol2.txt:distilled the rheum of intoxication.
vol2.txt:catacombs. I paused again, and this time I made bold to seize Fortunato
vol2.txt:vault overhead, in the fashion of the great catacombs of Paris. Three
vol2.txt:supports of the roof of the catacombs, and was backed by one of their
vol2.txt:that the intoxication of Fortunato had in a great measure worn off. The
vol2.txt:earliest indication I had of this was a low moaning cry from the depth
vol2.txt:me. I placed my hand upon the solid fabric of the catacombs, and felt
vol2.txt:My heart grew sick--on account of the dampness of the catacombs. I
vol2.txt:them. _In pace requiescat!_
vol2.txt:modification of that which ordinarily springs from the combativeness
vol2.txt:modification of combativeness, but in the case of that something which I
vol2.txt:it flow; he dreads and deprecates the anger of him whom he addresses;
vol2.txt:mortification of the speaker, and in defiance of all consequences) is
vol2.txt:catch myself pondering upon my security, and repeating, in a low
vol2.txt:experienced all the pangs of suffocation; I became blind, and deaf,
vol2.txt:seemed indicative of joy--but sorrow deformed it as she passed within
vol2.txt:to be nearly the sole covering to her delicate form; but the mid-summer
vol2.txt:of ungovernable crimson; and a slight shudder quivers about her delicate
vol2.txt:from curtains which rolled from their cornices like cataracts of molten
vol2.txt:not only by birth, but in education, an _Englishman_.
vol2.txt:delicately imagined wings. My glance fell from the painting to the
vol2.txt:catching some faint ray of light. I proceeded for many paces; but still
vol2.txt:my agony as I thought of such application of such a term.
vol2.txt:the vapour of heated iron! A suffocating odour pervaded the prison! A
vol2.txt:the reader that, from the long and weird catalogue of human miseries,
vol2.txt:at once, if necessary to a hundred well authenticated instances. One of
vol2.txt:application of the battery. One experiment succeeded another, and the
vol2.txt:were uttered; the syllabification was distinct. Having spoken, he fell
vol2.txt:which physicians have agreed to term catalepsy, in default of a more
vol2.txt:and, upon application of a mirror to the lips, we can detect a torpid,
vol2.txt:catalepsy, by the consequent suspicion excited, and, above all, by
vol2.txt:a cataleptic trance of more than usual duration and profundity. Suddenly
vol2.txt:of those who were aware of my proneness to catalepsy, lest, falling into
vol2.txt:subject to catalepsy. And now, at last, as if by the rush of an ocean,
vol2.txt:cattymount?" said a fourth; and hereupon I was seized and shaken
vol2.txt:them vanished the cataleptic disorder, of which, perhaps, they had been
vol2.txt:early education, or in the nature of his intellect, had tinged with
vol2.txt:art can but suggest. We may be instructed to build a "Cato," but we
vol2.txt:intricate, and seemed often as if returning in upon themselves, so
vol2.txt:still remained, but her character seemed to have undergone modification,
vol2.txt:to see, far down in the inverted heaven, the duplicate blooming of the
vol2.txt:a panoramic cataract of rubies, sapphires, opals, and golden onyxes,
vol2.txt:softer linden, red-bud, catalpa, and maple--these yet again by still
vol2.txt:convey. And then the stately grace of the clean, delicately-granulated
vol2.txt:locusts and catalpas.
vol2.txt:third the impudent bobolink--while three or four more delicate prisons
vol2.txt:Flowers, indeed, of gorgeous colours and delicate odour formed the sole
vol2.txt:not justly be termed a caricature,) I will not now venture to describe.
vol2.txt:altercation of violence with him, in which he was more than usually
vol2.txt:chambers communicating with each other, where slept the greater number
vol2.txt:immediately after the altercation just mentioned, finding every one
vol2.txt:flushed with cards and intoxication, I was in the act of insisting upon
vol2.txt:of novel follies, I added no brief appendix to the long catalogue of
vol2.txt:his intoxication, I thought, might partially, but could not altogether
vol2.txt:mischief. Poor justification this, in truth, for an authority so
vol2.txt:now the suffocating atmosphere of the crowded rooms irritated me beyond
vol2.txt:With a too unscrupulous confidence she had previously communicated to me
vol2.txt:thirty-two small, white and ivory-looking substances that were scattered
vol2.txt:indications of her presence, sighing upon me in the evening winds, or
vol2.txt:bewildered and intoxicated my brain. But as yet my soul had proved true
vol2.txt:to its vows, and the indications of the presence of Eleonora were still
vol2.txt:petrification.--_Kennedy_.
vol2.txt:eaten under the bark are readily recognizable. The most delicate of the
vol2.txt:(*12) _Schouw_ advocates a class of plants that grow upon living
vol2.txt:description: "'_The Hotte_, a decided caterpillar, or worm, is found
vol2.txt:electronic work, you indicate that you have read, understand, agree to
vol2.txt:located in the United States, we do not claim a right to prevent you from
vol2.txt:1.D.  The copyright laws of the place where you are located also govern
vol2.txt:from the public domain (does not contain a notice indicating that it is
vol2.txt:work, (b) alteration, modification, or additions or deletions to any
vol2.txt:501(c)(3) educational corporation organized under the laws of the
vol2.txt:Revenue Service.  The Foundation's EIN or federal tax identification
vol2.txt:The Foundation's principal office is located at 4557 Melan Dr. S.
vol2.txt:Fairbanks, AK, 99712., but its volunteers and employees are scattered
vol2.txt:throughout numerous locations.  Its business office is located at
vol2.txt:with these requirements.  We do not solicit donations in locations
vol3.txt:undertake a regular compilation and publication of the adventures in
vol3.txt:Barnard's, and both Augustus and myself were not a little intoxicated
vol3.txt:intoxicated, but that he was never more sober in his life. He was only
vol3.txt:intoxication--a state which, like madness, frequently enables the victim
vol3.txt:had assisted in hastening the catastrophe. He was now thoroughly
vol3.txt:he first discovered the extent of his intoxication, and felt himself
vol3.txt:supposed that a catastrophe such as I have just related would have
vol3.txt:been sheer fabrications) well adapted to have weight with one of
vol3.txt:dreading every moment that I should swoon amid the narrow and intricate
vol3.txt:which the dreadful deaths of thirst, famine, suffocation, and premature
vol3.txt:some unevenness on its surface, which a delicate sense of feeling might
vol3.txt:These I now threw over him, and before he could extricate himself, I had
vol3.txt:Fortunately he was so far overcome by intoxication as to be easily
vol3.txt:that if such an expression were indicative of merriment, the merriment
vol3.txt:precarious, as the men were continually intoxicated, and there was no
vol3.txt:to communicate with me by the way of the main hold. In any other
vol3.txt:turn round, he could not extricate himself. Peters at last let him out,
vol3.txt:duplicate of the forged letter from Mr. Ross. This had been the original
vol3.txt:last stage of intoxication. Like Peters, they made no scruple of talking
vol3.txt:every difficulty and danger in reaching me. Having extricated himself as
vol3.txt:communicated to me while we remained near the box. It was not
vol3.txt:intoxication, while the two others were with him, was a feint. He
vol3.txt:almost entirely, and gave no indications of hydrophobia, drinking a
vol3.txt:indications, too--such, for example, as there being no such thing as
vol3.txt:some tin tumblers which lay about, they were not as much intoxicated
vol3.txt:the apparition of Rogers was indeed a revivification of his disgusting
vol3.txt:without holding more than a speaking communication with any vessel
vol3.txt:The creaking and working of the mainmast, too, gave indication that it
vol3.txt:gave no indication of life whatever, and was bent nearly double across a
vol3.txt:rhodomontades, intermingled with howls and imprecations, while the
vol3.txt:of--hellish--utterly suffocating--insufferable, inconceivable. I gasped
vol3.txt:scattered about between the counter and the galley in the last and most
vol3.txt:bowsprit to a cathead. On his back, from which a portion of the shirt
vol3.txt:violent effect, and that they were all exceedingly intoxicated. With
vol3.txt:the voyage I had been in bad health, and was at all times of a delicate
vol3.txt:time, and in the most supplicating manner, begging him in the name of
vol3.txt:or twenty minutes, we contrived to catch some water by means of a sheet
vol3.txt:When I communicated this object to my companions, they uttered a feeble
vol3.txt:lightning, we turn our attention to the catching of water by means of
vol3.txt:distressing intoxication which had ensued upon drinking the port. The
vol3.txt:to evince symptoms of mortification. He complained of drowsiness and
vol3.txt:but lasted so short a time that we only succeeded in catching about
vol3.txt:cheeks hung so loosely as to prevent his masticating any food, or even
vol3.txt:of intoxication. We afterward endeavoured to relieve our sufferings by
vol3.txt:feet of me, and various other articles from the brig were scattered
vol3.txt:by which we had been hitherto enabled to catch rainwater, and of the jug
vol3.txt:catching the water, we might have filled one, if not both of them. As
vol3.txt:scattering their nests here and there, wherever they can find room,
vol3.txt:immediately over the spots indicated by the commander of the Atrevida,
vol3.txt:could discover no indication of land. These conflicting statements have
vol3.txt:degrees 58' W.--that is to say, very nearly upon the spot indicated as
vol3.txt:ourselves about the station indicated by Glass, and cruised for three
vol3.txt:from the vast number of birds to be seen, and from other indications,
vol3.txt:to the southward were observed to be of a snowy whiteness, indicating
vol3.txt:other usual indications of land, and although, south of the Shetlands,
vol3.txt:degree of gratification at having been instrumental, however remotely,
vol3.txt:head resembled a cat's, with the exception of the ears--these were
vol3.txt:roughly, commenced a half whine, half howl, strongly indicative of
vol3.txt:rocks were novel in their mass, their color, and their stratification;
vol3.txt:domesticated. The largest of these creatures resembled our common hog in
vol3.txt:birds in a state of entire domestication, going to sea periodically
vol3.txt:best chance of extricating ourselves from the dilemma, sacrificing him
vol3.txt:caterpillars or worms, they creep in shallow waters, in which, when low,
vol3.txt:our companions, examining, as we went along, the singular stratification
vol3.txt:AS soon as I could collect my scattered senses, I found myself nearly
vol3.txt:suffocated, and grovelling in utter darkness among a quantity of loose
vol3.txt:beyond the possibility of extricating him. I soon found that what he
vol3.txt:singular stratification of these soapstone hills; and the description
vol3.txt:for effecting the same purpose. Of this stratification the savages had
vol3.txt:catastrophe, and were not disappointed. First of all there came a smart
vol3.txt:never alighted, we had no opportunity of catching them.
vol3.txt:seacoast, distant not more than half a mile, with a view of catching
vol3.txt:_March 1st_. {*7}-Many unusual phenomena now--indicated that we were
vol3.txt:of the king-that the inhabitants of the group fabricated no other boats
vol3.txt:felt none. The countenance of Peters indicated nothing of this nature,
vol3.txt:of form. I can liken it to nothing but a limitless cataract, rolling
vol3.txt:water as it fell. The summit of the cataract was utterly lost in the
vol3.txt:the embraces of the cataract, where a chasm threw itself open to receive
vol3.txt:will be remembered, served only as a means of communication between the
vol3.txt:"hyacinthine!" I looked at the delicate outlines of the nose--and
vol3.txt:be eradicated by human means, I could not fall to observe a similar
vol3.txt:revivification was repeated; how each terrific relapse was only into a
vol3.txt:on account of her Presburg education, she placed before me a number of
vol3.txt:those of a cat. The pupils, too, upon any accession or diminution of
vol3.txt:have always advocated its existence. Modern discoveries, indeed, in what
vol3.txt:delicate fingers, upon one of which sparkled a diamond ring, which I
vol3.txt:delicate point--for a woman to urge, especially so; in mentioning it,
vol3.txt:confiding affection. Encouraged by her candor upon the delicate point of
vol3.txt:the delicate hand which offered the glasses for my inspection. They
vol3.txt:immense value as a gem. You perceive that, by a trifling modification
vol3.txt:"You wretch!" said I, catching my breath--"you--you--you villainous old
vol3.txt:Meantime I sank aghast into the chair which she had vacated. "Moissart
vol3.txt:scattered here and there within it, sufficiently well adapted to its
vol3.txt:indicated the region beyond to be under the Pest-ban, that, in
vol3.txt:bewildered in its noisome and intricate recesses.
vol3.txt:Had they not, indeed, been intoxicated beyond moral sense, their reeling
vol3.txt:paths more narrow and more intricate. Huge stones and beams falling
vol3.txt:jugs, pitchers, and flagons of every shape and quality, were scattered
vol3.txt:of intoxication. This gentleman was clothed from head to foot in a
vol3.txt:patronise. This delicate little creature, in the trembling of her wasted
vol3.txt:which tinged her otherwise leaden complexion, gave evident indications
vol3.txt:far below her under lip, and in spite of the delicate manner in which
vol3.txt:know, uncle, is that you would indicate the time precisely."
vol3.txt:electronic work, you indicate that you have read, understand, agree to
vol3.txt:located in the United States, we do not claim a right to prevent you from
vol3.txt:1.D.  The copyright laws of the place where you are located also govern
vol3.txt:from the public domain (does not contain a notice indicating that it is
vol3.txt:work, (b) alteration, modification, or additions or deletions to any
vol3.txt:501(c)(3) educational corporation organized under the laws of the
vol3.txt:Revenue Service.  The Foundation's EIN or federal tax identification
vol3.txt:The Foundation's principal office is located at 4557 Melan Dr. S.
vol3.txt:Fairbanks, AK, 99712., but its volunteers and employees are scattered
vol3.txt:throughout numerous locations.  Its business office is located at
vol3.txt:with these requirements.  We do not solicit donations in locations
vol4.txt:     Mystification
vol4.txt:upon this delicate point--some acute, some learned, some sufficiently
vol4.txt:character, Catch-word and No Cypher; wherein consult, also, marginal
vol4.txt:her side there stands a fat tabby cat, with a gilt toy-repeater tied to
vol4.txt:him look as handsome as the cat.
vol4.txt:the little gilt repeaters on the tails of the cat and pig.
vol4.txt:to see. But, worse than all, neither the cats nor the pigs could put
vol4.txt:poking, and squeaking and screeching, and caterwauling and squalling,
vol4.txt:one might catch a glimpse of the scoundrel through the smoke. There he
vol4.txt:"Come here!" [Here he took me by the arm.] "Your education may now
vol4.txt:found myself at Almack's. The rooms were crowded to suffocation.
vol4.txt:composing for the especial gratification (?) of him (the "Gazette")
vol4.txt:which these latter were communicated, nothing escaped to gratify the
vol4.txt:towards himself interfere with the gratification of my curiosity, and
vol4.txt:exceedingly neat parlor, containing, among other indications of refined
vol4.txt:were well educated; and my host was a world of good-humored anecdote
vol4.txt:au-chat--and, for the matter of that, none of their cat-au-rabbit
vol4.txt:whom you have, necessarily, heard; and, again, there are modifications
vol4.txt:shouts and imprecations were heard beneath the windows; and, immediately
vol4.txt:intoxicated to do duty, now sprang all at once to their feet and to
vol4.txt:delicate drink during dinner. And then, again, the frog-man croaked
vol4.txt:And now came the climax--the catastrophe of the drama. As no resistance,
vol4.txt:The "soothing system," with important modifications, has been resumed at
vol4.txt:perfectly scentless.' Fine that, and very delicate! Turn it about
vol4.txt:continued to fight valiantly, dead as he was. The application of this
vol4.txt:sensation-paper. In the present case your application is the most
vol4.txt:Horses they neighed. Cats they caterwauled. Dogs they danced. Danced!
vol4.txt:presented itself to view a church--a Gothic cathedral--vast, venerable,
vol4.txt:immense extent of the city. The door of the cathedral stood invitingly
vol4.txt:it is said the immense river Alfred passed, unscathed, and unwetted,
vol4.txt:the church in which I was, and the delicate architecture of the steeple.
vol4.txt:It might have been half an hour after this altercation when, as I was
vol4.txt:well have tried to lift the cathedral itself. Down, down, down it came,
vol4.txt:of your swaggerers, and nothing at all indelicate in her motions. She
vol4.txt:MYSTIFICATION
vol4.txt:vivid exemplifications. My acquaintance with Ritzner commenced at the
vol4.txt:make the science of mystification the study and the business of their
vol4.txt:Alma Mater. The deep, the poignant, the overwhelming mortification,
vol4.txt:some recent Parisian publications, backed by three or four desperate and
vol4.txt:afforded food for mystification. Of this, however, I was not aware;
vol4.txt:specification. That my opinions, however, are not the opinions to be
vol4.txt:concerning "Injuriae per applicationem, per constructionem, et per se,"
vol4.txt:ninth paragraph of the chapter of "Injuriae per applicationem, per
vol4.txt:applicationem, per constructionem, et per se. Having finished reading,
vol4.txt:      The cat and the fiddle
vol4.txt:copy is brief, and being headed with "Lost" only, indicates No. 2 Dick,
vol4.txt:will be preferred. Application should be made between the hours of ten
vol4.txt:precipitate--and it is not until the most rigid catechism in respect to
vol4.txt:Very soon, a strong suffocating odor assailed my nostrils; the house, I
vol4.txt:shop for cat peltries and other furs. Pundit knows, you know; there can
vol4.txt:the category Aries (that is to say Ram) nor under the category Hog, why
vol4.txt:at once indicate to them the true state of affairs--that of the binary
vol4.txt:as we do now, with a mere indication of the design to erect a monument
vol4.txt:gently opens to the sound of soft music, and lo! the most delicate of
vol4.txt:a mystification, intended especially for myself. I made up my mind, of
vol4.txt:refused, although I repeatedly urged them, to hold communication with
vol4.txt:indifferent looking, totally uneducated, and decidedly vulgar." The
vol4.txt:forever--to use one of her own delicate expressions--forever "on the tip
vol4.txt:could not, for that reason, quite forgive his incommunicativeness in the
vol4.txt:of his little bit of pleasant mystification. My first observation was
vol4.txt:with the qualifications of the dead--dead, with the propensities of
vol4.txt:deep guttural, I might still have continued to her the communication of
vol4.txt:most decided of atrocities while the tabby cat purred strenuously upon
vol4.txt:respiratory faculties rendered suffocation an accident entirely out of
vol4.txt:Seeing that I remained motionless (all my limbs were dislocated and my
vol4.txt:arousing the rest of the passengers, he communicated, in a very decided
vol4.txt:of mortification to me, nevertheless, that although I made several
vol4.txt:sleep, when two cats, of a greedy and vituperative turn, entering at a
vol4.txt:hole in the wall, leaped up with a flourish a la Catalani, and alighting
vol4.txt:themselves,) and, having communicated this opinion to one another, they
vol4.txt:days of a dog. Therein, he has dreamed of flames and suffocation--of
vol4.txt:expatiate--to be able to communicate with a person like yourself, who do
vol4.txt:stage-struck--horrible occurrence!--heard of "catching one's breath,"
vol4.txt:affair so delicate--so delicate, I repeat, and at the time involving the
vol4.txt:justification--followed in the columns of a Democratic Gazette. It was
vol4.txt:by the side, of that worthy and communicative little friend of mine,
vol4.txt:"Or a more delicate sense of the true beauties of Shakespeare? Be so
vol4.txt:mystery. Here, at least, there should be no chance for equivocation. I
vol4.txt:adventure for a livelihood, was somewhat ill-adapted to the delicate
vol4.txt:fling me over into the pit. Neck dislocated, and right leg capitally
vol4.txt:too much for my delicate state of body; and, discovering, at last, that
vol4.txt:no means, so respectable a profession. My location, to be sure, was an
vol4.txt:My eighth and last speculation has been in the Cat-Growing way. I have
vol4.txt:cats--so much so of late, that a petition for relief, most numerously
vol4.txt:enactments, it crowned all with the Cat-Act. In its original form, this
vol4.txt:law offered a premium for cat-heads (fourpence a-piece), but the Senate
vol4.txt:of the poetic sentiment. The proper gratification of the sentiment he
vol4.txt:peculiarities, either in his early education, or in the nature of his
vol4.txt:I repeat that in landscape arrangements, or collocations alone, is the
vol4.txt:no change, and subject to no modification. This being the case, we can
vol4.txt:disposition of the men at one period of a game can we predicate their
vol4.txt:designated spot, or even shift its location repeatedly during the
vol4.txt:his silence--his actions cannot implicate him in a falsehood--his words
vol4.txt:complicated crossings of the rays--crossings which are brought about by
vol4.txt:triplicate and triple--tinted suns.
vol4.txt:ever in their modifications of old forms--or, in other words, in
vol4.txt:for the which he justly regarded as an all-sufficient education for the
vol4.txt:purification {*3} which alone could efface its rectangular obscenities,
vol4.txt:the corruption you indicate did surely warrant us in believing. Men
vol4.txt:Touch had undergone a modification more peculiar. Its impressions were
vol4.txt:of the catastrophe itself, I know nothing. When, coming out from among
vol4.txt:modifications to which it might be subjected, were now the topics of
vol4.txt:in the rapid modification of the air. The red blood bounded tumultuously
vol4.txt:suffocation--anxiety--and, above all, that terrible state of existence
vol4.txt:and my dwelling is near to the Catacombs of Ptolemais, and hard by those
vol4.txt:electronic work, you indicate that you have read, understand, agree to
vol4.txt:located in the United States, we do not claim a right to prevent you from
vol4.txt:1.D.  The copyright laws of the place where you are located also govern
vol4.txt:from the public domain (does not contain a notice indicating that it is
vol4.txt:work, (b) alteration, modification, or additions or deletions to any
vol4.txt:501(c)(3) educational corporation organized under the laws of the
vol4.txt:Revenue Service.  The Foundation's EIN or federal tax identification
vol4.txt:The Foundation's principal office is located at 4557 Melan Dr. S.
vol4.txt:Fairbanks, AK, 99712., but its volunteers and employees are scattered
vol4.txt:throughout numerous locations.  Its business office is located at
vol4.txt:with these requirements.  We do not solicit donations in locations
vol5.txt:     Dedication
vol5.txt:delicate appreciation, or at least the elements of a proper sense. The
vol5.txt:        --Lucan--De Catone
vol5.txt:make up my mind to communicate the circumstances to my friend.
vol5.txt:a triplicate treasure in one person.
vol5.txt:intoxication, and looking fixedly but quietly into the tyrant's face,
vol5.txt:company; and rushing in with savage cries, among the crowd of delicately
vol5.txt:As he proceeded, the company grew more scattered, and his old uneasiness
vol5.txt:was in the constant habit of catching and kissing the female babies.
vol5.txt:question cui bono? very pointedly implicated Mr. Pennifeather. His
vol5.txt:pretty much intoxicated, and excessively red in the face, now took a
vol5.txt:been living like a houly imperor, and gitting the iddication and the
vol5.txt:wasn't mesilf thin that was mad as a Kilkenny cat I shud like to be
vol5.txt:cat at Mounseer Frog, and thin as smiling as all out o' doors at mesilf.
vol5.txt:THAT Pierre Bon-Bon was a _restaurateur_ of uncommon qualifications,
vol5.txt:the Cotes du Rhone. With him Sauterne was to Medoc what Catullus was to
vol5.txt:told you that Bon-Bon was a man of genius. His very cat knew it, and
vol5.txt:were visible in large letters Oeuvres de Bon-Bon. Thus was delicately
vol5.txt:of retouching a voluminous manuscript, intended for publication on the
vol5.txt:discover the words "Rituel Catholique" in white letters upon the back.
vol5.txt:contemplated publication, enlighten the human race, and at the same time
vol5.txt:thwarted in the outset of their application--and the restaurateur found
vol5.txt:joined lustily in the chorus, and the tabby cat, flying off at a
vol5.txt:of the cat. It must be confessed, he felt a little astonishment to see
vol5.txt:the white letters which formed the words "Rituel Catholique" on the
vol5.txt:could discover no indications of their having existed at any previous
vol5.txt:penetrating than your own. There is a cat I see in the corner--a pretty
vol5.txt:cat--look at her--observe her well. Now, Bon-Bon, do you behold the
vol5.txt:were Lucilius, and Catullus, and Naso, and Quintus Flaccus,--dear
vol5.txt:which I did not feel justified in indicating more unequivocally.)
vol5.txt:indicated the vast wealth of the deceased.
vol5.txt:The application of electricity to a mummy three or four thousand years
vol5.txt:course, gave no indication of galvanic susceptibility when brought in
vol5.txt:catapult, through a window into the street below.
vol5.txt:of the left corner of his mouth, and, by way of indemnification inserted
vol5.txt:since he had been consigned to the catacombs at Eleithias.
vol5.txt:thing among us in the old days. But the fact is, I fell into catalepsy,
vol5.txt:"that among the catacombs near the Nile there may exist other mummies of
vol5.txt:lived. Now this process of re-scription and personal rectification,
vol5.txt:mortification. I reached my hat, bowed to him stiffly, and took leave.
vol5.txt:than Shelley is their author. Their warm, yet delicate and ethereal
vol5.txt:should inculcate a morals and by this moral is the poetical merit of the
vol5.txt:I would nevertheless limit, in some measure, its modes of inculcation.
vol5.txt:poetical modes of inculcation. He must be theory-mad beyond redemption
vol5.txt:duplicate source of the light. But this mere repetition is not poetry.
vol5.txt:once a consequence and an indication of his perennial existence. It is
vol5.txt:versification although carrying the fanciful to the very verge of the
vol5.txt:Although the rhythm here is one of the most difficult, the versification
vol5.txt:_quite independent of that passion which is the intoxication of the
vol5.txt:by highly artificial verse, to inculcate what he supposed to be moral
vol5.txt:pathos, exquisitely delicate imagination and truthfulness-to anything of
vol5.txt:her face. Consider the great variety of truthful and delicate thought
vol5.txt:            _I DEDICATE THIS VOLUME_
vol5.txt:         Arose with a duplicate horn--
vol5.txt:         Distinct with its duplicate horn.
vol5.txt:by N. P. Willis: "We are permitted to copy (in advance of publication)
vol5.txt:of versification, and consistent sustaining of imaginative lift and
vol5.txt:several advantages for versification over our own, chiefly through
vol5.txt:versification an entirely different effect. We could wish the capacities
vol5.txt:publication, another revision of the poem, similar to the current
vol5.txt:in the "Home Journal," it was copied into various publications with the
vol5.txt:which publication it appeared in January, 1850, three months after the
vol5.txt:8. The sonnet, "To My Mother" (Maria Clemm), was sent for publication to
vol5.txt:     "Should catch the note, as it doth float--up from the damned Earth.
vol5.txt:          *On the fair Capo Deucato, and sprang
vol5.txt:     The bee, feeding upon its blossom, becomes intoxicated.
vol5.txt:     attendant upon intoxication are its less holy pleasures--
vol5.txt:     They weep:--from off their delicate stems
vol5.txt:publication in "Scribner's Magazine" for September, 1875; but as proofs
vol5.txt:electronic work, you indicate that you have read, understand, agree to
vol5.txt:located in the United States, we do not claim a right to prevent you from
vol5.txt:1.D.  The copyright laws of the place where you are located also govern
vol5.txt:from the public domain (does not contain a notice indicating that it is
vol5.txt:work, (b) alteration, modification, or additions or deletions to any
vol5.txt:501(c)(3) educational corporation organized under the laws of the
vol5.txt:Revenue Service.  The Foundation's EIN or federal tax identification
vol5.txt:The Foundation's principal office is located at 4557 Melan Dr. S.
vol5.txt:Fairbanks, AK, 99712., but its volunteers and employees are scattered
vol5.txt:throughout numerous locations.  Its business office is located at
vol5.txt:with these requirements.  We do not solicit donations in locations

```
**Counting 'dog'**

```
[h.dewit@a-les1-08: ~/Documents/Poe]% grep -c 'dog' vol*.txt               [12]
vol1.txt:10
vol2.txt:17
vol3.txt:23
vol4.txt:25
vol5.txt:13
[h.dewit@a-les1-08: ~/Documents/Poe]% grep -c -i 'dog' vol*.txt            [13]
vol1.txt:10
vol2.txt:17
vol3.txt:23
vol4.txt:28
vol5.txt:13

```
**Everytime 'dog' is mentioned**

```
[h.dewit@a-les1-08: ~/Documents/Poe]% grep -i 'dog' vol*.txt               [14]
vol1.txt:at hand, for the use of customers, I threw myself doggedly into it,
vol1.txt:o'clock--Legrand, Jupiter, the dog, and myself. Jupiter had with him the
vol1.txt:complaisance. His demeanor was dogged in the extreme, and "dat deuced
vol1.txt:embarrassment lay in the yelpings of the dog, who took exceeding
vol1.txt:dogged air of deliberation, tied the brute's mouth up with one of his
vol1.txt:dog having been unmuzzled, we turned in profound silence towards home.
vol1.txt:interrupted by the violent howlings of the dog. His uneasiness, in the
vol1.txt:articles taken out were deposited among the brambles, and the dog
vol1.txt:the intervention of the dog at the precise moment in which he appeared,
vol1.txt:suspicion, in spite of the dogmatic ignorance of Le Soleil, that they
vol2.txt:his meerschaum, "although I have been guilty of certain doggrel myself."
vol2.txt:given to the rhetorical dogma, that metaphor, or simile, may be made
vol2.txt:servitude, no doubt,) such as we keep on our dogs, only much wider
vol2.txt:dogs, only a little larger and more savage; and that these vermin had
vol2.txt:cats and dogs have any difficulty in seeing objects that do not exist at
vol2.txt:a shake, just as a dog does in coming out of the water, and thus rid
vol2.txt:the metal, and we arrive at once (in spite of all the school dogmas) at
vol2.txt:dog, I need hardly be at the trouble of explaining the nature or the
vol2.txt:had birds, gold-fish, a fine dog, rabbits, a small monkey, and _a cat_.
vol2.txt:monkey, or even the dog, when by accident, or through affection, they
vol2.txt:paid to the man's asseveration; but his evident terror, and the dogged
vol2.txt:it was they who had buried me as a dog--nailed up in some common
vol2.txt:existence of Ellison I fancy that I have seen refuted the dogma, that in
vol2.txt:out my hand, however, in token of amity--and I never yet knew the dog
vol2.txt:his impertinent and dogged interference with my purposes, were not more
vol2.txt:arrival at the academy! And then his dogged and meaningless imitation
vol2.txt:villain! you shall not--you shall not dog me unto death! Follow me, or I
vol3.txt:tired, he added, of lying in bed on such a fine night like a dog, and
vol3.txt:as himself, and quite as tired as he was of lying in bed like a dog,
vol3.txt:of my Newfoundland dog Tiger, and the odd manner of his caresses I well
vol3.txt:by his caresses. Most people love their dogs--but for Tiger I had an
vol3.txt:to the water; and the grown dog repaid the obligation, about three years
vol3.txt:and I could in no manner account for it. As the dog seemed distressed,
vol3.txt:dog. I concluded at once that he had devoured the whole of my supply
vol3.txt:it to the dog's nose, and endeavored to make him understand that he must
vol3.txt:mattress. It arose from the demeanor of the dog.
vol3.txt:dog sprang with a loud growl toward my throat. The whole weight of his
vol3.txt:beneath the dog, and a few moments would place me completely in his
vol3.txt:Spanish dog or American grizzly bear. At the time spoken of, he had on a
vol3.txt:Tiger, who immediately leaped into the berth and lay down. The dog had
vol3.txt:This slip of paper being tied upon the dog, he was now put down the
vol3.txt:over the impediments in our way with the huge dog in his arms--a feat
vol3.txt:that I could do but little. The dog would not leave his hold upon the
vol3.txt:behind his back. The dog was still growling over Jones; but, upon
vol3.txt:of the bulldog. The meat was tender, but excessively rank and fishy,
vol3.txt:flopped like the ears of a dog. The teeth were of the same brilliant
vol3.txt:the forenoon--and then set forth alone, or attended only by a dog, upon
vol3.txt:of dogged indifference to matters and things in general, was not the
vol3.txt:Kate--but it was a dog's existence that he led me, after all. From my
vol3.txt:promise to cut me off with a shilling. I was a sad dog, it is true--but
vol4.txt:fire-dogs. There is constantly a rousing fire, and a huge pot over it,
vol4.txt:doll, a poll; a poor, old, good-for-nothing-to-nobody, log, dog, hog, or
vol4.txt:the case with a bevy of dogs at night. It occasionally happens, however,
vol4.txt:dog, or drowned in a gutter. But to proceed.
vol4.txt:think me of it, there are a couple of very excellent bull-dogs in the
vol4.txt:Pompey, and my little lap-dog Diana, whom I had brought with me from
vol4.txt:Horses they neighed. Cats they caterwauled. Dogs they danced. Danced!
vol4.txt:stirred up by a trifle! The dogs danced! I--I could not! They frisked--I
vol4.txt:Sweet creature! she too has sacrificed herself in my behalf. Dogless,
vol4.txt:capable of a joke, verbal or practical:--the old bull-dog at
vol4.txt:every day dips one of them in his soup, makes his dog jump for it,
vol4.txt:maturity, the diddler, with the diddler's dog, calls upon the friend,
vol4.txt:diddler, when up jumps the diddler's dog and devours it forthwith.
vol4.txt:behavior of his dog, and expresses his entire readiness to cancel the
vol4.txt:"No. 110 Dog Street"
vol4.txt:the column of "dogs lost," and then the two columns of "wives and
vol4.txt:ancient dogmaticians to have determined by which of their two roads it
vol4.txt:dogs" that we read of in fable. He says that they started with
vol4.txt:the earth--unless we except the case of the "prairie dogs," an exception
vol4.txt:admirable form of government--for dogs.
vol4.txt:the rug, and the very water dog wheezed assiduously under the table,
vol4.txt:Being little of a cynic, I had all the sentiments of a dog. The hangman,
vol4.txt:has been his mortal enemy. In the dog-days his days have been the
vol4.txt:days of a dog. Therein, he has dreamed of flames and suffocation--of
vol4.txt:"We had rather hot work of it, that you may say. Now, you dog, slip
vol4.txt:little dog, too, was quite fat and up to all varieties of snuff. He
vol4.txt:avaricious, but my dog was. I allowed him a third of the profit, but he
vol4.txt:of Ellison, I fancy, that I have seen refuted the dogma--that in
vol5.txt:the walls of every kennel, to traffic with the dogs of the earth? Lower
vol5.txt:to vituperate my deceased friend, Toby Dammit. He was a sad dog, it is
vol5.txt:true, and a dog's death it was that he died; but he himself was not to
vol5.txt:and sold him for dog's meat.
vol5.txt:large water-dog was acquainted with the fact, and upon the approach
vol5.txt:not altogether unworthy of a dog. It is, however, true that much of this
vol5.txt:nearly bordering upon the sublime. In its size both dogs and men
vol5.txt:large black water-dog we have spoken of before, and settling himself
vol5.txt:uproariously, while the black dog, crouching down upon his haunches,
vol5.txt:laugh like the dog, or by shrieks to betray the indecorous trepidation
vol5.txt:"That's a lie!" repeated the restaurateur, dogmatically; "that's
vol5.txt:notice:--simply kicking the dog, and requesting him to be quiet. The
vol5.txt:  You dog! and make it up, I say, this minute!
[h.dewit@a-les1-08: ~/Documents/Poe]%      

```
**Inspecting Adobe's 'phone home' behaviour**

```
[h.dewit@a-les1-08: ~]% netstat -a | grep -i 'adobe'                                          [22]
8ec9ed6ef7cadf83 stream      0      0                0 8ec9ed6ef7cae04b                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-h.dewit
8ec9ed6eedb49ebb stream      0      0                0 8ec9ed6eedb4afeb                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-h.dewit
8ec9ed6eedb49f83 stream      0      0 8ec9ed6ee710973b                0                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-h.dewit

```