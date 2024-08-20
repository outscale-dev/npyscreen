#!/usr/bin/python
import curses
import osc_npyscreen
import unittest

osc_npyscreen.add_test_input_from_iterable('This is a test')
osc_npyscreen.TEST_SETTINGS['TEST_INPUT'].append(curses.KEY_DOWN)
osc_npyscreen.TEST_SETTINGS['TEST_INPUT'].append("^X")
osc_npyscreen.TEST_SETTINGS['CONTINUE_AFTER_TEST_INPUT'] = True

class TestForm(osc_npyscreen.FormWithMenus):
    def create(self):
        self.myTitleText = self.add(osc_npyscreen.TitleText, name="Events (Form Controlled):", editable=True)

class TestApp(osc_npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", TestForm)

class Tests(unittest.TestCase):
    def setUp(self):
        self.testApp = TestApp()
        
    def test_text_entry(self):
        osc_npyscreen.TEST_SETTINGS['TEST_INPUT'] = [ch for ch in 'This is a test']
        osc_npyscreen.TEST_SETTINGS['TEST_INPUT'].append(curses.KEY_DOWN)
        
        
        

if __name__ == '__main__':
    #TestMemory()
    A = TestApp()
    A.run()