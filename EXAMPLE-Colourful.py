#!/usr/bin/env python
import oscscreen
class TestApp(oscscreen.NPSApp):
	def main(self):
		# These lines create the form and populate it with widgets.
		# A fairly complex screen in only 8 or so lines of code - a line for each control.
		oscscreen.setTheme(oscscreen.Themes.ColorfulTheme)
		F = oscscreen.ActionFormWithMenus(name = "Welcome to Oscscreen",)
		t = F.add(oscscreen.TitleText, name = "Text:", )
		fn = F.add(oscscreen.TitleFilename, name = "Filename:")
		dt = F.add(oscscreen.TitleDateCombo, name = "Date:")
		s = F.add(oscscreen.TitleSlider, out_of=12, name = "Slider")
		ml= F.add(oscscreen.MultiLineEdit, 
			value = """try typing here! Mutiline text, press ^R to reformat.\n""", 
			max_height=5, rely=9)
		ms= F.add(oscscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One", 
				values = ["Option1","Option2","Option3"], scroll_exit=True)
		ms2= F.add(oscscreen.TitleMultiSelect, max_height=4, value = [1,], name="Pick Several", 
				values = ["Option1","Option2","Option3"], scroll_exit=True)
		
		# This lets the user play with the Form.
		F.edit()


if __name__ == "__main__":
	App = TestApp()
	App.run()
