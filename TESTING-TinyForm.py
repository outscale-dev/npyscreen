#!/usr/bin/env python
# encoding: utf-8
import osc_npyscreen

class TinyForm(osc_npyscreen.FormBaseNew):
    DEFAULT_NEXTRELY = 0
    BLANK_LINES_BASE   = 0

class TestApp(osc_npyscreen.NPSApp):
    def main(self):
        F  = TinyForm(name = "Welcome to Oscscreen", 
                        framed=False, 
                        lines=1, 
                        columns=0, 
                        minimum_lines = 1)
        ms = F.add(osc_npyscreen.TitleText, name='Test', )        
        F.edit()
if __name__ == "__main__":
    App = TestApp()
    App.run()   
