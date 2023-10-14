#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:45:03 2023

@author: adamfaucher
"""
def is_professional(sender_name):
    professional = False
    professional_titles = ['Professor', 'Prof', 'Dr.', 'Dr ', 'Mrs.','Mrs ', 'Mr.', 'Mr ', 'Ms.', 'Ms ', 'Mx.', 'Mx ','Pastor', 'Father', 'Dean', 'Sir', 'Madam', 'Dame']
    for title in professional_titles:
        if title in sender_name:
            professional = True
    return professional
            
def generate_email_greeting(sender_name, professional=True):
    '''
    Generates an email greeting and determines the sender_type based on user input.

    :param user_name: The name of the user or sender.
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
