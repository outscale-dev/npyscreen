#!/usr/bin/env python
import osc_npyscreen
import EXAMPLE

#def Mainloop(scr):
#	while 1:
#		sampleform()
#
#def sampleform():
#	F = osc_npyscreen.Form(name = "Welcome to Oscscreen")
#	t = F.add(osc_npyscreen.TitleText, name = "Text:")
#	p = F.add(osc_npyscreen.TitlePassword, name = "Password:")
#	fn = F.add(osc_npyscreen.TitleFilename, name = "Filename:")
#	s = F.add(osc_npyscreen.TitleSlider, out_of=12, name = "Slider")
#	ml= F.add(osc_npyscreen.MultiLineEdit, value = "try typing here! Mutiline text, press ^R to reformat.", max_height=4)
#	ms= F.add(osc_npyscreen.MultiSelect, max_height=4, value = [1,], values = ["Option1","Option2","Option3"], scroll_exit=True)

class TestMem(osc_npyscreen.NPSApp):
	def main(self):
		F = osc_npyscreen.Form(name = "Welcome to Oscscreen")
		t = F.add(osc_npyscreen.TitleText, name = "Text:")
		p = F.add(osc_npyscreen.TitlePassword, name = "Password:")
		fn = F.add(osc_npyscreen.TitleFilename, name = "Filename:")
		s = F.add(osc_npyscreen.TitleSlider, out_of=12, name = "Slider")
		ml= F.add(osc_npyscreen.MultiLineEdit, value = "try typing here! Mutiline text, press ^R to reformat.", max_height=3, rely=7)
		ms= F.add(osc_npyscreen.MultiSelect, max_height=4, value = [1,], values = ["Option1","Option2","Option3"], scroll_exit=True)
		
		F.display()
		
if __name__ == "__main__":
	Test = TestMem()
	Test.run()
	while 1:
		Test = TestMem()
		Test.main()
	
