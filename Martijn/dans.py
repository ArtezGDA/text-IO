"""waltz choreographer.py
    Copyright (c) <2015> <Martijn de Lange>
    function: printing waltz choreography"""

import curses # import curses the program that enables you to print text on given coordinats
import time  #import time the program that enables you to pause the proces of drawing text by saying to the computer:come back at a given time

screen = curses.initscr()# making a window
screen.addstr( 2, 1, "|/")  #the placement of the words en letters can be changed within screen.addstr()
screen.addstr( 3, 0, "voor", curses.A_BOLD)     #you can also make an accent within the dance by changing the font to bold by saying:curses.A_BOLD

time.sleep(1)
screen.refresh()
screen.addstr( 2, 6, "|/")
screen.addstr( 3, 6, "zij")

time.sleep(1)
screen.refresh()
screen.addstr( 2, 12, "/")
screen.addstr( 3, 10, "sluit")
time.sleep(1)
screen.refresh()
screen.addstr( 4, 16, "\->")
screen.addstr( 4, 14, "v", curses.A_BOLD)
time.sleep(1)
screen.refresh()
screen.addstr( 5, 14, "o", curses.A_BOLD)
screen.refresh()
screen.addstr( 6, 14, "o", curses.A_BOLD)
screen.refresh()
screen.addstr( 7, 14, "r", curses.A_BOLD)


screen.refresh()

screen.addstr( 9, 16, "/->")
screen.addstr( 9, 14, "z")
time.sleep(1)
screen.refresh()
screen.addstr( 10, 14, "i")
screen.addstr( 11, 14, "j")

screen.refresh()


time.sleep(0.5)
screen.addstr( 13, 16, "\->")
screen.addstr( 13, 14, "s")
screen.addstr( 14, 14, "l")
screen.addstr( 15, 14, "u")
screen.addstr( 16, 14, "i")
screen.addstr( 17, 14, "t")
screen.refresh()

time.sleep(0.5)
screen.addstr( 19, 16, "/->")
screen.addstr( 19, 14, "z")
screen.addstr( 20, 14, "i")
screen.addstr( 21, 14, "j")
screen.refresh()

time.sleep(0.5)
screen.addstr( 19, 16, "/->")
screen.addstr( 19, 14, "z")
screen.addstr( 20, 14, "i")
screen.addstr( 21, 14, "j")
screen.refresh()

time.sleep(1)
screen.addstr( 22, 19, "\|")
screen.addstr( 22, 14, "voor",curses.A_BOLD)
screen.refresh()
time.sleep(1)
screen.addstr( 22, 28, "/->")
screen.addstr( 22, 24, "zij")
screen.refresh()
time.sleep(0.7)
screen.addstr( 22,48, "\->")
screen.addstr( 22, 34, "kruis achter")
screen.refresh()

time.sleep(0.3)
screen.addstr( 22,63, "/|")
screen.addstr( 22, 54, "draai om ")
screen.refresh()

time.sleep(1.25)
screen.addstr( 22,71, "\|")
screen.addstr( 22, 67, "voor ",curses.A_BOLD)
screen.refresh()
time.sleep(1)
screen.addstr( 22,77, "\|")
screen.addstr( 22, 74, "zij")
screen.refresh()


screen.addstr( 22,77, "\|")
screen.addstr( 22, 74, "zij")
screen.refresh()



screen.addstr( 19,75, "\->")
screen.addstr( 19, 74, "v",curses.A_BOLD)
screen.addstr( 18, 70, "o",curses.A_BOLD)
screen.addstr( 17, 66, "o",curses.A_BOLD)
screen.addstr( 16, 63, "r",curses.A_BOLD)
time.sleep(1)
screen.refresh()

screen.addstr( 14,63, "/->")
screen.addstr( 13, 62, "z")
screen.addstr( 12, 61, "i")
screen.addstr( 11, 60, "j")
time.sleep(1)
screen.refresh()

screen.addstr( 9, 60, "\|")
screen.addstr( 8, 60, "d")
screen.addstr( 7, 60, "r")
screen.addstr( 6, 60, "a")
screen.addstr( 5, 60, "a")
screen.addstr( 4, 60, "i")
time.sleep(1)
screen.refresh()


screen.addstr( 3,57, "/|")
screen.addstr( 3, 59, "voor",curses.A_BOLD)
time.sleep(1)
screen.refresh()


screen.addstr( 3,64, "/|")
screen.addstr( 3,66, "kruis")
screen.refresh()
time.sleep(1)

screen.addstr( 3,72, "/|")
screen.addstr( 3,74, "achter")
time.sleep(1)
screen.refresh()

screen.addstr( 2,63, "/|")
screen.addstr( 2, 65, "voor",curses.A_BOLD)
time.sleep(1)
screen.refresh()

screen.addstr( 2,54, "/_")
screen.addstr( 2, 56, "zij")
time.sleep(1)
screen.refresh()

screen.addstr( 3,54, "/_")
screen.addstr( 4,56, "a")
screen.addstr( 5,55, "c")
screen.addstr( 6,54, "h")
screen.addstr( 7,53, "t")
screen.addstr( 8,52, "e")
screen.addstr( 9,51, "r")
time.sleep(1)
screen.refresh()

screen.addstr( 10,47, "/_",curses.A_BOLD)
screen.addstr( 11,47, "k",curses.A_BOLD)
screen.addstr( 12,45, "r",curses.A_BOLD)
screen.addstr( 13,43, "u",curses.A_BOLD)
screen.addstr( 14,41, "i",curses.A_BOLD)
screen.addstr( 15,39, "s",curses.A_BOLD)
time.sleep(1)
screen.refresh()

screen.addstr( 15,36, "/_")
screen.addstr( 14,35, "v")
screen.addstr( 13,34, "o")
screen.addstr( 12,33, "o")
screen.addstr( 11,32, "r")
time.sleep(1)
screen.refresh()

screen.addstr( 10,29, "/_")
screen.addstr( 9,28, "z")
screen.addstr( 8,27, "i")
screen.addstr( 7,26, "j")
time.sleep(1)
screen.refresh()

time.sleep(1)
screen.addstr( 5,25, "/_")
screen.addstr( 4,24, "s")
screen.addstr( 3,23, "l")
screen.addstr( 2,22, "u")
screen.addstr( 1,21, "i")
screen.addstr( 0,20, "t")
screen.refresh()



screen.getch() # with screen.getch() you are telling the curses program to go back to the terminal usual design
curses.endwin() #with curses.endwin() you end the session by hitting a key

