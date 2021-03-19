#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import os

x = os.system('cmd /k "date"')
print(x)

'''
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
result = subprocess.run(['dir','/w'], stdout=subprocess.PIPE)
print(result.stdout)
'''
