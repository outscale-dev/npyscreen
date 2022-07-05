import oscscreen

class MyTestApp(oscscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())

class MainForm(oscscreen.Form):
    def create(self):
        self.add(oscscreen.Textfield, color='CRITICAL', value='Testing Testing')
        self.color = "CRITICAL"
        pass

def main():
    TA = MyTestApp()
    TA.run()


if __name__ == '__main__':
    main()
