#!/usr/bin/python
import osc_npyscreen
import curses
import curses.ascii

def mainloop(scr):
	S = osc_npyscreen.Form()
	display=S.add_widget(osc_npyscreen.TitleText, name=unicode('Hello\267World!','latin-1').encode('utf-8'))
	display.value = name=unicode('Hello\267World!','latin-1').encode('utf-8')
	S.display()
	S.edit()
if __name__ == "__main__":
	curses.wrapper(mainloop)
