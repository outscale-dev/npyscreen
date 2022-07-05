#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import oscscreen

import inspect
import oscscreen
from oscscreen.widget import Widget

def main(*args):
    members = inspect.getmembers(oscscreen)
    for m in members:
        name, cl = m
        if isinstance(m, oscscreen.Form):
            print "True"
        


if __name__ == '__main__':
    main()
    #oscscreen.wrapper(main)

