#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:28:47 2023

@author: adamfaucher
"""

def generate_email_closing(name, professional=True):
    '''
    A function that generates a professional "Sincerly, [USER NAME]" style closing to the email
    
    :Param
    :Return
    '''
    if professional:
        return f"Sincerely, {name}"
    else:
        return f" -{name}"


        