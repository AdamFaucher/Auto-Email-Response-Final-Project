#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:45:03 2023

@author: adamfaucher
"""
def is_professional(sender_name):
    '''
    Decides if the tone should be professional or not based on the sender's name and a list of titles.

    :param: sender_name : str : name of the sender of the email that needs to be responded to

    Returns: professional : bool : True if the email should be professional, False if not
    '''
    professional = False
    professional_titles = ['Professor', 'Prof', 'Dr.', 'Dr ', 'Mrs.','Mrs ', 'Mr.', 'Mr ', 'Ms.', 'Ms ', 'Mx.', 'Mx ','Pastor', 'Father', 'Dean', 'Sir', 'Madam', 'Dame']
    for title in professional_titles:
        if title in sender_name:
            professional = True
    return professional
            
def generate_email_greeting(sender_name, professional=True):
    '''
    Generates an email greeting from the sender's name and tone.

    :param sender_name : str : The name of the sender.
    :param professional : bool : the tone of the email, True if the email should be professional, False if not
    :return: A tuple containing the email greeting and sender_type.
    '''
    greeting = f"Hello {sender_name},"
    if professional == True:
        greeting = f"Dear {sender_name},"
    else:
        greeting = f"Hi {sender_name},"
    return greeting, professional

if __name__ == "__main__":
    sender_name = input("Enter sender name: ")
    professional = is_professional(sender_name)
    greeting, sender_type = generate_email_greeting(sender_name, professional)
    
    print("\nGenerated Greeting:", greeting)
    print("Sender is professional:", sender_type)
