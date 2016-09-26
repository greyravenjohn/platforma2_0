#
import curses as c
import curses.panel as p

class Window:
    """window class"""

    def __init__( self, stdscr, vertical = 3, horizontal = 20, x = 2, y = 2 ):
        #self.max_x = stdscr.getmaxyx()[1] -1
        #self.max_y = stdscr.getmaxyx()[0] -1
        self.v = vertical
        self.h = horizontal
        self.x = x
        self.y = y
        #self.x = int( ( self.max_x - self.h )/x )
        #self.y = int( ( self.max_y - self.v )/y )

        del stdscr

        self.view = "X"
        self.center_view = int( ( ( self.h )/2 ) - len( self.view ) )

        self.window = c.newwin( self.v, self.h, self.y, self.x )
        self.window.box()
        self.window.move( 1, self.center_view )
        self.window.addstr( self.view )
        self.window_panel = p.new_panel( self.window )
        self.window_panel.bottom()

        self.show_changes()

    def show_changes( self ):
        p.update_panels()
        c.doupdate()

    def display_fresh( self, view, row = 1):
        #funkcja wpisujaca nowa wartosc do okna
        #kazda pozycja listy to nowy wysrodokwany wiersz
        #opcionalna wartosc row to wiersz od korego zaczyna sie (-1)
        self.view_list = view.split('\n')
        self.no = row

        for i in self.view_list:
            self.center_view = int ( ( self.h - len( i ) )/2 )
            self.window.addstr( self.no, self.center_view, i )
            self.no +=1 
            
        self.window.refresh()

