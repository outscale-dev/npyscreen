#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import osc_npyscreen

import inspect
import osc_npyscreen
from osc_npyscreen.widget import Widget

def main(*args):
    members = inspect.getmembers(osc_npyscreen)
    for m in members:
        name, cl = m
        if isinstance(m, osc_npyscreen.Form):
            print "True"
        


if __name__ == '__main__':
    main()
    #osc_npyscreen.wrapper(main)

