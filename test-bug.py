# -*- coding: utf-8 -*-
# filename: npsapp.py

from osc_npyscreen import NPSApp
from osc_npyscreen import Form

class App(NPSApp):
   def main(self):
       form = Form(name='Welcome to Oscscreen')
       form.edit()

if __name__ == '__main__':
   app = App()
   app.run()

