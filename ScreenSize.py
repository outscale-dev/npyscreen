#!/usr/bin/env python
import oscscreen
import curses

class TestApp(oscscreen.NPSApp):
	def main(self):
		self.F = oscscreen.Form(name = "Welcome to Oscscreen")
		self.t = self.F.add(oscscreen.TitleText, name = "Text:")
		while 1:
			self.update_values()
			curses.flash()
			curses.napms(100)
	
	def update_values(self):
		self.t.value = "y: %s x: %s" % (self.F._max_physical())
		self.F.display()



if __name__ == '__main__':
	A = TestApp()
	A.run()
