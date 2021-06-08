#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 00:17:27 2021

@author: williammcintyre
"""

# isPhoneNumber with regular Expressions
# Will McIntyre

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # \d means a digit character
mo = phoneNumRegex.search('My number is 519-781-4510') 
print('phone number found: '+ mo.group())