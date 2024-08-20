#!/usr/bin/env python
import osc_npyscreen

class TestApp(osc_npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F = osc_npyscreen.ActionFormWithMenus(name = "Welcome to Oscscreen",)
        f = F.add(osc_npyscreen.TitleFixedText, name = "Fixed Text:" , value="This is fixed text")
        #t10= F.add(osc_npyscreen.TitleText,  use_two_lines=None, name = "10:" ,max_width = 10)
        #t15 = F.add(osc_npyscreen.TitleText, use_two_lines=None, name = "15:" ,max_width = 15)
        t20=  F.add(osc_npyscreen.TitleText,  use_two_lines=None, name = "20:" ,max_width = 20)
        t25 = F.add(osc_npyscreen.TitleText,  use_two_lines=None, name = "25:" ,max_width = 25)
        t30 = F.add(osc_npyscreen.TitleText,  use_two_lines=None, name = "30:" ,max_width = 30)
        t35 = F.add(osc_npyscreen.TitleText,  use_two_lines=None, name = "35:" ,max_width = 35)
        t40 = F.add(osc_npyscreen.TitleText,  use_two_lines=None, name = "40:" ,max_width = 40)
        t45=  F.add(osc_npyscreen.TitleText,  use_two_lines=None, name = "45:" ,max_width = 45)
    
        tmax = F.add(osc_npyscreen.TitleText,  use_two_lines=None, name = "Max" ,max_width = False)
        tn20 = F.add(osc_npyscreen.TitleText,  use_two_lines=None, name = "n20:" ,max_width = -20)
        #tn200= F.add(osc_npyscreen.TitleText,  use_two_lines=None, name = "n200:" ,max_width = -200)
        
    
        F.edit()

if __name__ == "__main__":
    App = TestApp()
    App.run()
