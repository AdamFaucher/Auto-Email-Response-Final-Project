#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:27:03 2023

@author: adamfaucher
"""

def generate_greeting(sender_name):
    '''
    A function that generates a professional "Hello, [SENDER NAME]," style greeting to the email
        
    :Param string of the email sender's name'
    :Return larger string of the email sender's with the greeting'
    '''
    print('Input sender name:')
    sender_name = input()
    
    if 'Professor' in sender_name:
        greeting_string = 'Dear ' + sender_name + ','
        sender_type_Prof = True
    if 'Dr' in sender_name:
        greeting_string = 'Dear ' + sender_name + ','
        sender_type_prof = True
    elif 'Professor' or 'Dr' not in sender_name:
        greeting_string = 'Hello ' + sender_name + ','
        sender_type_prof = False
    return (greeting_string, sender_type_Prof)

generate_greeting('Professor Andrews')