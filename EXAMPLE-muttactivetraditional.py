#!/usr/bin/env python
import oscscreen
import curses


class ActionControllerSearch(oscscreen.ActionControllerSimple):
    def create(self):
        self.add_action('^/.*', self.set_search, True)
    
    def set_search(self, command_line, widget_proxy, live):
        self.parent.value.set_filter(command_line[1:])
        self.parent.wMain.values = self.parent.value.get()
        self.parent.wMain.display()


class FmSearchActive(oscscreen.FormMuttActiveTraditional):
    ACTION_CONTROLLER = ActionControllerSearch

class TestApp(oscscreen.NPSApp):
    def main(self):
        F = FmSearchActive()
        F.wStatus1.value = "Status Line "
        F.wStatus2.value = "Second Status Line "
        F.value.set_values([str(x) for x in range(500)])
        F.wMain.values = F.value.get()
        
        F.edit()


if __name__ == "__main__":
    App = TestApp()
    App.run()
