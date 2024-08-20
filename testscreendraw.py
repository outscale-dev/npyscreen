#!/usr/bin/env python

import osc_npyscreen
class A(osc_npyscreen.NPSApp):
    def main(self):
        scr = F()
        scr.edit()

class F(osc_npyscreen.TitleFooterForm):
    def create(self):
        b = []
        for n in range(self.widget_useable_space(rely=self.nextrely)[0]):
            b.append(self.add(osc_npyscreen.Button, name="%s %s %s" % (n, self.BLANK_LINES_BASE, self.widget_useable_space()[0])))

if __name__ == '__main__':
    a = A()
    a.run()