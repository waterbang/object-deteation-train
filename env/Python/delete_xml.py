# -*- coding: utf-8 -*-
"""
Created on Sun Sep 03 22:01:25 2017

@author: Administrator
"""


#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".xml"):
                os.remove(os.path.join(root,name))         
                print ("Delete File: " + os.path.join(root, name))

# test
if __name__ == "__main__":
    path = '/Users/waterbang/Desktop/tensorflow/dog/images/test/campus'
    del_files(path)
