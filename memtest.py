#!/usr/bin/env python
import oscscreen
import EXAMPLE

#def Mainloop(scr):
#	while 1:
#		sampleform()
#
#def sampleform():
#	F = oscscreen.Form(name = "Welcome to Oscscreen")
#	t = F.add(oscscreen.TitleText, name = "Text:")
#	p = F.add(oscscreen.TitlePassword, name = "Password:")
#	fn = F.add(oscscreen.TitleFilename, name = "Filename:")
#	s = F.add(oscscreen.TitleSlider, out_of=12, name = "Slider")
#	ml= F.add(oscscreen.MultiLineEdit, value = "try typing here! Mutiline text, press ^R to reformat.", max_height=4)
#	ms= F.add(oscscreen.MultiSelect, max_height=4, value = [1,], values = ["Option1","Option2","Option3"], scroll_exit=True)

class TestMem(oscscreen.NPSApp):
	def main(self):
		F = oscscreen.Form(name = "Welcome to Oscscreen")
		t = F.add(oscscreen.TitleText, name = "Text:")
		p = F.add(oscscreen.TitlePassword, name = "Password:")
		fn = F.add(oscscreen.TitleFilename, name = "Filename:")
		s = F.add(oscscreen.TitleSlider, out_of=12, name = "Slider")
		ml= F.add(oscscreen.MultiLineEdit, value = "try typing here! Mutiline text, press ^R to reformat.", max_height=3, rely=7)
		ms= F.add(oscscreen.MultiSelect, max_height=4, value = [1,], values = ["Option1","Option2","Option3"], scroll_exit=True)
		
		F.display()
		
if __name__ == "__main__":
	Test = TestMem()
	Test.run()
	while 1:
		Test = TestMem()
		Test.main()
	
