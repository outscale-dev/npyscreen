#!/usr/bin/python
import curses
import oscscreen

class TestForm(oscscreen.Form):
    def create(self):
        self.myFixedText = self.add(oscscreen.TitleFixedText, name="Events (Form Controlled):", editable=False)
        self.myFixedText2 = self.add(oscscreen.TitleFixedText, name="Events (App Controlled):", editable=False)
        self.myFixedText.value = '1'
        self.myFixedText2.value = '1'
        self.mytext = self.add(oscscreen.TitleText, name = "Text:",)
        self.add_event_hander("TESTEVENT", self.ev_test_event_handler)
        
    def ev_test_event_handler(self, event):
        self.myFixedText.value = int(self.myFixedText.value) + 1
        self.myFixedText.display()
        
    def while_waiting(self):
        self.parentApp.queue_event(oscscreen.Event("TESTEVENT"))
    

class EventApp(oscscreen.StandardApp):
    def onStart(self):
        #self.keypress_timeout_default = 2
        self.addForm("MAIN", TestForm)
        self.add_event_hander("TESTEVENT", self.ev_test_event_handler)
    
    def while_waiting(self):
        self.queue_event(oscscreen.Event("TESTEVENT"))
        
        # The following puts more events on the queue than the default app can ever process.
        # 100 added each time, but only 50 dealt with.
        # this creates a memory leak.
        #for x in range(100):
        #    self.queue_event(oscscreen.Event("TESTEVENT"))
    
    def ev_test_event_handler(self, event):
        wg = self.getForm("MAIN").myFixedText2
        wg.value = int(wg.value) + 1
        wg.display()
    
def TestMemory():
    class TestApp(oscscreen.NPSApp):
        def main(self):
            F = TestForm()
            while True:
                F.display()
    
    TestApp().run()
    
        
    while True:
        #A = EventApp()
        
        TF = TestForm()  
    
if __name__ == '__main__':
    #TestMemory()
    A = EventApp()
    A.run()