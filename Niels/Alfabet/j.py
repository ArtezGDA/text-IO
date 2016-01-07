import curses
import random
import time

for myChar in range(10):
    randomNum = random.randint(33, 126)
    myChar = chr(randomNum)

screen = curses.initscr()
screen.addstr( 20, 84, str(randomNum))

screen.addstr( 22, 84, str(randomNum))
screen.addstr( 23, 84, str(randomNum))
screen.addstr( 24, 84, str(randomNum))
screen.addstr( 25, 84, str(randomNum))
screen.addstr( 26, 84, str(randomNum))
screen.addstr( 27, 84, str(randomNum))
screen.addstr( 28, 84, str(randomNum))
screen.addstr( 29, 84, str(randomNum))
screen.addstr( 30, 84, str(randomNum))
screen.addstr( 31, 84, str(randomNum))
screen.addstr( 32, 83, str(randomNum))
screen.addstr( 33, 81, str(randomNum))
screen.addstr( 32, 75, str(randomNum))
screen.addstr( 33, 77, str(randomNum))
screen.addstr( 31, 75, str(randomNum))

screen.addstr( 16, 104, str(randomNum))
screen.addstr( 17, 104, str(randomNum))
screen.addstr( 18, 104, str(randomNum))
screen.addstr( 19, 104, str(randomNum))
screen.addstr( 20, 104, str(randomNum))
screen.addstr( 21, 104, str(randomNum))
screen.addstr( 22, 104, str(randomNum))
screen.addstr( 23, 104, str(randomNum))
screen.addstr( 24, 104, str(randomNum))
screen.addstr( 25, 104, str(randomNum))
screen.addstr( 26, 104, str(randomNum))
screen.addstr( 27, 104, str(randomNum))
screen.addstr( 28, 104, str(randomNum))
screen.addstr( 29, 104, str(randomNum))
screen.addstr( 30, 104, str(randomNum))
screen.addstr( 31, 104, str(randomNum))
screen.addstr( 32, 103, str(randomNum))
screen.addstr( 33, 101, str(randomNum))
screen.addstr( 32, 95, str(randomNum))
screen.addstr( 33, 97, str(randomNum))
screen.addstr( 31, 95, str(randomNum))


screen.getch()
curses.endwin()

