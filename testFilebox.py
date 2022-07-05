import oscscreen

class MyTestApp(oscscreen.NPSAppManaged):
    def onStart(self):
        self.addFormClass("MAIN", MainForm)

class MainForm(oscscreen.FileSelector):
    pass

def main():
    TA = MyTestApp()
    TA.run()

def test_function(scr):
    t = oscscreen.selectFile('~/',)
    oscscreen.notify_confirm(title='Selected File', message=t)
if __name__ == '__main__':
    #main()
    print(oscscreen.wrapper(test_function))
