#
import curses as c
import curses.panel as p

class Window:
    """window class"""

    def __init__( self, stdscr, vertical = 3, horizontal = 20 ):
        self.max_x = stdscr.getmaxyx()[1] -1
        self.max_y = stdscr.getmaxyx()[0] -1

        self.v = vertical
        self.h = horizontal
        self.x = int( ( self.max_x - self.h )/2 )
        self.y = int( ( self.max_y - self.v )/2 )

        del stdscr

        self.view = "X"
        self.center_view = int( ( (self.h )/2 ) - len( self.view ) )

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

    def display_fresh_1_row( self, view ):
        self.view = view
        self.center_view = int( ( (self.h )/2 ) - len( self.view ) )
        
        self.window.addstr( 1, self.center_view, self.view )
        self.window.refresh()

    def display_fresh_n_rows( self, view, rows = None ):
        
        if( rows != None ):
            self.rows = rows

        self.view_list = view.split
        self.rows = len( self.view_list )

        for i in rows
