#!/usr/bin/env python
# encoding: utf-8

import osc_npyscreen
#osc_npyscreen.disableColor()
class TestApp(osc_npyscreen.NPSApp):
    def main(self):
        F  = osc_npyscreen.Form(name = "Welcome to Oscscreen",)
        ms = F.add(osc_npyscreen.Button, name="Button", max_width=7, rely = -5, relx = -13)
        ml = F.add(osc_npyscreen.TitleMultiLine, name="Multiline", relx = -55, rely = 5, max_height=12, values = [1,2,3])
        
        F.edit()

if __name__ == "__main__":
    App = TestApp()
    App.run()   
