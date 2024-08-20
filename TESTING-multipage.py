#!/usr/bin/env python
# encoding: utf-8

import osc_npyscreen
#osc_npyscreen.disableColor()
class TestApp(osc_npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F = osc_npyscreen.FormMultiPageActionWithMenus(name = "Welcome to Oscscreen",)

        # NB The following is a very bad coding style
        # And is intended for testing purposes only.
        # A real application needing to display 80 text lines would use one of the 
        # multiline classes.
        for n in range(80):
            F.add_widget_intelligent(osc_npyscreen.TitleText, name = "Text %s:" % n,)
        
        F.switch_page(0)

        F.edit()
        


if __name__ == "__main__":
    App = TestApp()
    App.run()   
