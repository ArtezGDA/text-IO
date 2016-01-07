## Motivy<br>

----
`Motivy` provides you every 15 min of motivational messages such as **"Good Job!"**,**"You can do this!"**,**"Awesome!"**. These messages will be seen through a Note of the Notification center so they will pop-up immediately every 15 min.

The Notifications and sounds are adjustable to your own preferences.

### Motivy?
The program is dedicated to give people a "little push in the back"". You can put these `Motivy` on in the terminal (when you need them) and off (When you can handle it all by yourself) in the activity center under Untilities.


### Install

To install `Motivy`, open your terminal and type: 

```
curl http://www.link.... 
```

Or download the [DownloadMotivy.zip](TheDictionary/..........py) file in this directory.

The sounds in the file need to be put in your sounds folder before you can use `Motivy`.


- Switch to the Finder
- On the Finder menu bar click Go
- Then paste this directory "path" into the pop-up that appears.

<b>Keyboard shortcut</b>
When you're in Finder, ctrl+Tab+g and type:

```
/System/Library/Sounds
```
or

```
/Users/< username >/Library/Sounds/
```


You should be at the "Sounds" folder. Go ahead and drag the `Motivy` sounds into this folder seperately. 

sounds: 

 - yes
 - Applause
 - Cheer
 - Woohoo

### Usage
To put `Motivy` on you should open your Terminal and type: 

```
python Motivy.py
```
To put `Motivy` off:

- Switch to the Finder
- On the Finder menu bar click Go
- Select Utilities
- Select Activity monitor
- Stop Python

<b>Keyboard shortcut</b>
When you're in Finder, simultaneously press the Shift-Command-U key combination


### Adjusting Motivy

You want to change the sounds into your own sounds? Make sure you have some .aiff file to put into the sounds folder (noted above) and you change the [Motivy JSON](Tool/Motivyinput.json) sound names in the code.

You want to change Motivy's messages? change the text in the [Motivy JSON](Tool/Motivyinput.json)
file.

### Screenshots

![image](Screenshots/Motivity.png)
![image](Screenshots/Motivity1.png)
![image](Screenshots/Motivity2.png)


### Dependencies:

- MAC OSC (Applescript)


### License
The MIT License (MIT)

Copyright (c) 2015 Graphic Design Arnhem at ArtEZ Academy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.