#!/usr/bin/env python
# encoding: utf-8


# The system here is an experimental one. See documentation for details.




import oscscreen
class TestApp(oscscreen.NPSApp):
    def main(self):
        Options = oscscreen.OptionList()
        
        # just for convenience so we don't have to keep writing Options.options
        options = Options.options
        
        options.append(oscscreen.OptionFreeText('FreeText', value='', documentation="This is some documentation."))
        options.append(oscscreen.OptionMultiChoice('Multichoice', choices=['Choice 1', 'Choice 2', 'Choice 3']))
        options.append(oscscreen.OptionFilename('Filename', ))
        options.append(oscscreen.OptionDate('Date', ))
        options.append(oscscreen.OptionMultiFreeText('Multiline Text', value=''))
        options.append(oscscreen.OptionMultiFreeList('Multiline List'))
        
        try:
            Options.reload_from_file('/tmp/test')
        except FileNotFoundError:
            pass        
        
        F  = oscscreen.Form(name = "Welcome to Oscscreen",)

        ms = F.add(oscscreen.OptionListDisplay, name="Option List", 
                values = options, 
                scroll_exit=True,
                max_height=None)
        
        F.edit()
        
        Options.write_to_file('/tmp/test')

if __name__ == "__main__":
    App = TestApp()
    App.run()   
