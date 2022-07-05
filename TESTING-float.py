#!/usr/bin/env python
# encoding: utf-8

import oscscreen
#oscscreen.disableColor()
class TestApp(oscscreen.NPSApp):
    def main(self):
        F  = oscscreen.Form(name = "Welcome to Oscscreen",)
        ms = F.add(oscscreen.Button, name="Button", max_width=7, rely = -5, relx = -13)
        ml = F.add(oscscreen.TitleMultiLine, name="Multiline", relx = -55, rely = 5, max_height=12, values = [1,2,3])
        
        F.edit()

if __name__ == "__main__":
    App = TestApp()
    App.run()   
