import curses
import random
import time

for myChar in range(10):
    randomNum = random.randint(33, 126)
    myChar = chr(randomNum)

screen = curses.initscr()
screen.addstr( 32, 81, str(randomNum))
screen.addstr( 32, 75, str(randomNum))
screen.addstr( 33, 79, str(randomNum))
screen.addstr( 33, 77, str(randomNum))
screen.addstr( 31, 74, str(randomNum))
screen.addstr( 30, 74, str(randomNum))
screen.addstr( 29, 75, str(randomNum))
screen.addstr( 29, 81, str(randomNum))
screen.addstr( 28, 77, str(randomNum))
screen.addstr( 28, 79, str(randomNum))
screen.addstr( 30, 81, str(randomNum))
screen.addstr( 30, 79, str(randomNum))
screen.addstr( 30, 77, str(randomNum))

screen.addstr( 16, 95, str(randomNum))
screen.addstr( 17, 95, str(randomNum))
screen.addstr( 18, 95, str(randomNum))
screen.addstr( 19, 95, str(randomNum))
screen.addstr( 20, 95, str(randomNum))
screen.addstr( 21, 95, str(randomNum))
screen.addstr( 22, 95, str(randomNum))
screen.addstr( 23, 95, str(randomNum))
screen.addstr( 24, 95, str(randomNum))
screen.addstr( 25, 95, str(randomNum))
screen.addstr( 26, 95, str(randomNum))
screen.addstr( 27, 95, str(randomNum))
screen.addstr( 28, 95, str(randomNum))
screen.addstr( 29, 95, str(randomNum))
screen.addstr( 30, 95, str(randomNum))
screen.addstr( 31, 95, str(randomNum))
screen.addstr( 32, 95, str(randomNum))
screen.addstr( 33, 95, str(randomNum))
screen.addstr( 33, 97, str(randomNum))
screen.addstr( 33, 99, str(randomNum))
screen.addstr( 33, 101, str(randomNum))
screen.addstr( 33, 103, str(randomNum))
screen.addstr( 33, 105, str(randomNum))
screen.addstr( 33, 107, str(randomNum))
screen.addstr( 33, 109, str(randomNum))
screen.addstr( 33, 111, str(randomNum))
screen.addstr( 25, 97, str(randomNum))
screen.addstr( 25, 99, str(randomNum))
screen.addstr( 25, 101, str(randomNum))
screen.addstr( 25, 103, str(randomNum))
screen.addstr( 25, 105, str(randomNum))
screen.addstr( 16, 95, str(randomNum))
screen.addstr( 16, 97, str(randomNum))
screen.addstr( 16, 99, str(randomNum))
screen.addstr( 16, 101, str(randomNum))
screen.addstr( 16, 103, str(randomNum))
screen.addstr( 16, 105, str(randomNum))
screen.addstr( 16, 107, str(randomNum))
screen.addstr( 16, 109, str(randomNum))
screen.addstr( 16, 111, str(randomNum))


screen.getch()
curses.endwin()

