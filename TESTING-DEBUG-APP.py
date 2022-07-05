#!/usr/bin/python
import curses
import oscscreen
import unittest

oscscreen.add_test_input_from_iterable('This is a test')
oscscreen.TEST_SETTINGS['TEST_INPUT'].append(curses.KEY_DOWN)
oscscreen.TEST_SETTINGS['TEST_INPUT'].append("^X")
oscscreen.TEST_SETTINGS['CONTINUE_AFTER_TEST_INPUT'] = True

class TestForm(oscscreen.FormWithMenus):
    def create(self):
        self.myTitleText = self.add(oscscreen.TitleText, name="Events (Form Controlled):", editable=True)

class TestApp(oscscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", TestForm)

class Tests(unittest.TestCase):
    def setUp(self):
        self.testApp = TestApp()
        
    def test_text_entry(self):
        oscscreen.TEST_SETTINGS['TEST_INPUT'] = [ch for ch in 'This is a test']
        oscscreen.TEST_SETTINGS['TEST_INPUT'].append(curses.KEY_DOWN)
        
        
        

if __name__ == '__main__':
    #TestMemory()
    A = TestApp()
    A.run()