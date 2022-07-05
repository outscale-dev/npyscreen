#!/bin/env python
import oscscreen

class MainFm(oscscreen.Form):
    def create(self):
        self.mb = self.add(oscscreen.MonthBox,
                    use_datetime = True)


class TestApp(oscscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainFm)


if __name__ == "__main__":
    A = TestApp()
    A.run()
