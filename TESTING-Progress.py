import osc_npyscreen


class ProcessBar(osc_npyscreen.Slider):
    def __init__(self, *args, **keywords):
        super(ProcessBar, self).__init__(*args, **keywords)
        self.editable = False
        
class ProcessBarBox(osc_npyscreen.BoxTitle):          
    _contained_widget = ProcessBar



class TestApp(osc_npyscreen.NPSApp):
    def main(self):
        F = osc_npyscreen.Form(name = "Welcome to Oscscreen",)
        s = F.add(ProcessBarBox, max_height=3, out_of=12, value=5, name = "Text:")
        
        #s.editable=False


        # This lets the user play with the Form.
        F.edit()


if __name__ == "__main__":
    App = TestApp()
    App.run()   
