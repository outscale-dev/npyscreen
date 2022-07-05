#!/usr/bin/env python
import oscscreen
class TestApp(oscscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        oscscreen.setTheme(oscscreen.Themes.ColorfulTheme)
        F = oscscreen.SplitForm(name = "Welcome to Oscscreen",)
        t = F.add(oscscreen.Textfield, name = "Text:", )
        t1 = F.add(oscscreen.TitleText, name = "Text:", )
        t2 = F.add(oscscreen.TitleMultiSelect, name="Testing", values=range(200))
        # This lets the user play with the Form.
        F.edit()


if __name__ == "__main__":
    App = TestApp()
    App.run()
