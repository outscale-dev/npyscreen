import oscscreen


class ProcessBar(oscscreen.Slider):
    def __init__(self, *args, **keywords):
        super(ProcessBar, self).__init__(*args, **keywords)
        self.editable = False
        
class ProcessBarBox(oscscreen.BoxTitle):          
    _contained_widget = ProcessBar



class TestApp(oscscreen.NPSApp):
    def main(self):
        F = oscscreen.Form(name = "Welcome to Oscscreen",)
        s = F.add(ProcessBarBox, max_height=3, out_of=12, value=5, name = "Text:")
        
        #s.editable=False


        # This lets the user play with the Form.
        F.edit()


if __name__ == "__main__":
    App = TestApp()
    App.run()   
