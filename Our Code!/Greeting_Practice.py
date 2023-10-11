#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:45:03 2023

@author: adamfaucher
"""

def generate_email_greeting(sender_name):
    '''
    Generates an email greeting and determines the sender_type based on user input.

    :param user_name: The name of the user or sender.
    '''
    sender_type = "Unknown"
    greeting = f"Hello {sender_name},"

    if "Professor" in sender_name:
        sender_type = "Professional"
    elif "Dr." in sender_name:
        sender_type = "Professional"
    elif "Mr." in sender_name:
        sender_type = "Professional"
    elif "Ms." in sender_name:
        sender_type = "Professional"
    elif "Mrs." in sender_name:
        sender_type = "Professional"

    return greeting, sender_type

if __name__ == "__main__":
    sender_name = input("Enter sender name: ")
    greeting, sender_type = generate_email_greeting(sender_name)
    
    print("\nGenerated Greeting:")
    print(greeting)
    print("Sender Type:", sender_type)
