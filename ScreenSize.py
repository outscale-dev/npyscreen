#!/usr/bin/env python
import osc_npyscreen
import curses

class TestApp(osc_npyscreen.NPSApp):
	def main(self):
		self.F = osc_npyscreen.Form(name = "Welcome to Oscscreen")
		self.t = self.F.add(osc_npyscreen.TitleText, name = "Text:")
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
