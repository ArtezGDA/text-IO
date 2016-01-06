##Cowsay Conversation

###Omschrijving
Cowsay is een pratende koe die zegt wat je typt. Als je niet van koeien houdt, geen probleem er zijn ook andere dieren die je kan gebruiken. Naast dieren zijn er nog een paar andere figuren. 

Met deze cowsay versie kun je de dieren een conversatie met elkaar aan laten gaan.

###Installeer
Voor u cowsay kan instaleren moet u eerst Homebrew instaleren. Dit doet u op de volgende manier, open de terminal en kopier/plak de hieronder genoemde terminal commando's en druk ENTER.</br>

```
xcode-select --install
```

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
```
brew doctor
```

Installeer cowsay op uw computer systeem. </br>
Het kan geïnstalleerd worden met één van deze terminal commando:

```
brew install cowsay
```
```
sudo apt-get install cowsay
```
```
yum install cowsay
```

Open de terminal en plak één de hierboven genoemde terminal commando. Druk daarna op ENTER.

Download de map met python-bestanden op uw computer en verplaatsen ze naar een logische locatie op uw computer. Open de terminal zoals in de voorbeeld hieronder:

```
cd documents
cd cowsay_conversation
python bestandsnaam.py
ENTER
```

###Screenshots

![3 conversaties](screenshot.jpg)

###Voorbeelden van hoe te gebruiken
De volgende code gebruiken in Sublime Text:</br>

<b>word</b>="In de hal van kasteel Elseneur."</br>
stdout, stderr = subprocess.Popen(</br>
                     ['<b>cowsay</b>', <b>word</b>]).communicate()</br></br>                                          
In het gedeelte <b>word = "......"</b> type je de tekst die de koe moet zeggen.</br>
In het gedeelte <b>'cowsay'</b> kun je een dier kiezen. Als je een andere dier wilt dan een koe heb je de volgende commando nodig: <b>'cowsay', '-f', 'vader-koala'</b></br></br>

Terminal commando: 

```
cowsay -l Enter
```
Geeft je een lijst met alle mogelijke cows:

$ cowsay -l
Cow files in /usr/share/cowsay/cows:</br>
apt beavis.zen bong bud-frogs bunny calvin cheese cock cower daemon default
dragon dragon-and-cow duck elephant elephant-in-snake eyes flaming-sheep
ghostbusters gnu head-in hellokitty kiss kitty koala kosh luke-koala
mech-and-cow meow milk moofasa moose mutilated pony pony-smaller ren sheep
skeleton snowman sodomized-sheep stegosaurus stimpy suse three-eyes turkey
turtle tux unipony unipony-smaller vader vader-koala www

###Extra benodigheden
De onderstaande gegeven kopieren en boven in de code plakken.</br>

```
!/usr/bin/env python
 encoding: utf-8
```
 ```
import subprocess
```

Cowsay: cowfiles.cow

###License (MIT License) 

SublimeCowsay is released under the MIT license.

Copyright © 2015 Lydienne Albertoe albertoe@live.nl

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
