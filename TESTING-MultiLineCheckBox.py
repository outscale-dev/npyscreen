#!/usr/bin/env python
# encoding: utf-8
import oscscreen
#oscscreen.disableColor()


class MultiSelectWidgetTesting(oscscreen.MultiSelect):
    _contained_widgets = oscscreen.CheckBoxMultiline
    _contained_widget_height = 2
    
    def display_value(self, vl):
        return vl



class TestApp(oscscreen.NPSApp):
    def main(self):
        value_list = [
            ["This is", "the first"],
            ["This is", "the second"],
            ["This is", "the third"],
            ["This is", "the fourth"],
        ]
        F  = oscscreen.Form(name = "Welcome to Oscscreen",)
        #t  = F.add(oscscreen.CheckBoxMultiline, max_height=4, name = ["This is a ", "multiline text box."])
        #t  = F.add(oscscreen.CheckBoxMultiline, max_height=4, name = ["This is a second", "multiline text box."])
        t = F.add(MultiSelectWidgetTesting, max_height=7, name="Testing", values=value_list, slow_scroll=False)
        
        # This lets the user play with the Form.
        F.edit()
        
if __name__ == "__main__":
    App = TestApp()
    App.run()   
