import oscscreen

class MyTestApp(oscscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm(lines=47))

class MainForm(oscscreen.Form):
    def create(self):
        vl = []
        for x in range(100):
            vl.append("Value %s" % x)
        self.add(oscscreen.MultiSelect, values=vl)

def main():
    TA = MyTestApp()
    TA.run()


if __name__ == '__main__':
    main()
