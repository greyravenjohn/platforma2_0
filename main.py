#!/usr/bin/env python3
import curses as c
import curses.panel as p
import socket
import time
from windows_curses import *

def main():

    stdscr = c.initscr()
    c.start_color()
    c.noecho()
    c.curs_set(0)
    stdscr.keypad(1)
    stdscr.border(0)
    stdscr.timeout(100)

    max_y, max_x = stdscr.getmaxyx()

    mode = Window( stdscr, 3, 14, int((max_x)/5)-10, 2 )
    a = "MODE A"
    b = "MODE B"
    mode.display_fresh( a )

    sys = Window( stdscr, 4, 14, int((max_x)/5)-10, 5 )
    s = "00:00:00\nlocalhost"
    sys.display_fresh( s )
    set_host = socket.gethostname()

    echo = Window( stdscr, 4, 14, int((max_x)/5)-10, 9 )
    d = "SONAR:\n00.00cm" 
    echo.display_fresh( d )

    info = Window( stdscr, 9, 24, int((2*max_x)/3), 2 )
    e = "MODE A:\n      \nKEY_UP\nKEY_DOWN\nKEY_LEFT\nKEY_RIGHT\nMODE A/B: a/b"
    f = "MODE B:\n      \n      \nSTART: s\nSTOP: d \n         \nMODE A/B: a/b"
    info.display_fresh( e )

    status = Window( stdscr, 3, 14, int((max_x)/4), 5 )
    g = "x"
    status.display_fresh( g )
    
    mode_a = True
    mode_b = False

    running = True
    while( running ):
        key = stdscr.getch()
        if( key == 27 ):    #Esc
            running = False
            break
        elif( key == 97 ):  #a
            mode_a = True
            mode_b = False
            mode.display_fresh( a )
        elif( key == 98 ):  #b
            mode_a = False
            mode_b = True
            mode.display_fresh( b )

        if( mode_a ):
            if( key == c.KEY_UP ):
                status.display_fresh( chr(key) )
            elif( key == c.KEY_DOWN ):
                status.display_fresh( chr(key) )
            elif( key == c.KEY_LEFT ):
                status.display_fresh( chr(key) )
            elif( key == c.KEY_RIGHT ):
                status.display_fresh( chr(key) )
            else:
                pass
            info.display_fresh( e )
        if( mode_b ):
            if( key == 115 ):   #s
                status.display_fresh( chr(key) )
            elif( key == 100 ): #d
                status.display_fresh( chr(key) )
            else:
                pass
            info.display_fresh( f )
        #
        set_time = time.strftime( "%H:%M:%S" )
        s = set_time + '\n' + set_host
        sys.display_fresh( s )
        #

    c.endwin()


if( __name__ == "__main__"):
    main()
