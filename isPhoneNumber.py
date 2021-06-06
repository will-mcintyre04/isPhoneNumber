#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 00:01:24 2021

@author: williammcintyre
"""

# Phone Number Function
# Will McIntyre

def inPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (4, 7):
        if not text[i].isdecimal():
            return False
    if text[8] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
