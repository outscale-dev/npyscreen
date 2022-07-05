# -*- coding: utf-8 -*-
# filename: npsapp.py

from oscscreen import NPSApp
from oscscreen import Form

class App(NPSApp):
   def main(self):
       form = Form(name='Welcome to Oscscreen')
       form.edit()

if __name__ == '__main__':
   app = App()
   app.run()

