import osc_npyscreen

class MyTestApp(osc_npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())

class MainForm(osc_npyscreen.Form):
    def create(self):
        self.add(osc_npyscreen.Textfield, color='CRITICAL', value='Testing Testing')
        self.color = "CRITICAL"
        pass

def main():
    TA = MyTestApp()
    TA.run()


if __name__ == '__main__':
    main()
