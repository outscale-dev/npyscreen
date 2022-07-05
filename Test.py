import oscscreen

class myEmployeeForm(oscscreen.Form):
    def afterEditing(self):
        self.parentApp.NEXT_ACTIVE_FORM = None

    def create(self):
       self.myName        = self.add(oscscreen.TitleText, name='Name')
       self.myDepartment = self.add(oscscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
       self.myDate        = self.add(oscscreen.TitleDateCombo, name='Date Employed')

class MyApplication(oscscreen.NPSAppManaged):
   def onStart(self):
       self.addForm('MAIN', myEmployeeForm, name='New Employee')
       # A real application might define more forms here.......
       
if __name__ == '__main__':
   TestApp = MyApplication().run()
   print "All objects, baby."

