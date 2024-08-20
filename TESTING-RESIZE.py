#!/usr/bin/env python
import osc_npyscreen
class TestApp(osc_npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        osc_npyscreen.setTheme(osc_npyscreen.Themes.ColorfulTheme)
        F = osc_npyscreen.SplitForm(name = "Welcome to Oscscreen",)
        t = F.add(osc_npyscreen.Textfield, name = "Text:", )
        t1 = F.add(osc_npyscreen.TitleText, name = "Text:", )
        t2 = F.add(osc_npyscreen.TitleMultiSelect, name="Testing", values=range(200))
        # This lets the user play with the Form.
        F.edit()


if __name__ == "__main__":
    App = TestApp()
    App.run()
