#!/usr/bin/python
import osc_npyscreen
import curses
import curses.ascii

def mainloop(scr):
    S = osc_npyscreen.Form()
    display=S.add_widget(osc_npyscreen.TitleText, name="Key name:")
    S.display()
    while 1:
        S.curses_pad.keypad(1)
        curses.cbreak()
        curses.raw()
        curses.cbreak()
        #S.curses_pad.nodelay(1)
        ch = S.curses_pad.getch()
        try:
            display.value="%s" % (curses.keyname(ch))
        except:
            pass
        S.display()

if __name__ == "__main__":
    curses.wrapper(mainloop)

