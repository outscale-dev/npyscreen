#!/bin/env python
import osc_npyscreen

class MainFm(osc_npyscreen.Form):
    def create(self):
        self.mb = self.add(osc_npyscreen.MonthBox,
                    use_datetime = True)


class TestApp(osc_npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainFm)


if __name__ == "__main__":
    A = TestApp()
    A.run()
