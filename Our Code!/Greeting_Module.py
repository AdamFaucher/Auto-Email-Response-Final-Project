#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:27:03 2023

@author: adamfaucher
"""

def generate_greeting(sender_name):
    #https://www.w3schools.com/python/ref_func_input.asp
    #Used the above funciton to understand the input function
    
    '''
    A function that generates a professional "Hello, [SENDER NAME]," style greeting to the email, using the input function
    
    :Param string of the email sender's name'
    :Return larger string of the email sender's with the greeting'
    '''
    if 'Professor' in sender_name:
        greeting_string = 'Dear, ' + sender_name
        sender_type_Prof = True
    if 'Dr' in sender_name:
        greeting_string = 'Dear, ' + sender_name
        sender_type_Prof = True
    elif 'Professor' or 'Dr' not in sender_name:
        greeting_string = 'Hello, ' + sender_name    
        sender_type_Prof = False
    return greeting_string