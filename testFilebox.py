import osc_npyscreen

class MyTestApp(osc_npyscreen.NPSAppManaged):
    def onStart(self):
        self.addFormClass("MAIN", MainForm)

class MainForm(osc_npyscreen.FileSelector):
    pass

def main():
    TA = MyTestApp()
    TA.run()

def test_function(scr):
    t = osc_npyscreen.selectFile('~/',)
    osc_npyscreen.notify_confirm(title='Selected File', message=t)
if __name__ == '__main__':
    #main()
    print(osc_npyscreen.wrapper(test_function))
