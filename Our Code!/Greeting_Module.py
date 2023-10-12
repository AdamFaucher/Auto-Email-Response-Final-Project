#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:27:03 2023

@author: adamfaucher
"""
def generate_email_greeting(sender_name, is_professional=True):
    '''
    A function that generates a professional "Hello, [SENDER NAME]," style greeting to the email
        
    :Param string of the email sender's name'
    :Return larger string of the email sender's with the greeting'
    '''
    if is_professional:
        return f"Dear {sender_name},"
    else:
        return f"Hello {sender_name}"

