#!/usr/bin/env python
# encoding: utf-8

import oscscreen
#oscscreen.disableColor()
class TestApp(oscscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = oscscreen.Form(name = "Welcome to Oscscreen",)

        ms = F.add(oscscreen.MultiLineActionWithShortcuts, max_height=4, value = [1,], name="Pick One", 
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        
        # This lets the user play with the Form.
        F.edit()

        print ms.get_selected_objects()

if __name__ == "__main__":
    App = TestApp()
    App.run()   
