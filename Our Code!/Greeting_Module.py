#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:27:03 2023

@author: cqlambert
"""

def generate_greeting(emails):
    '''
    A function that generates a professional "Hello, [SENDER NAME]," style greeting to the email
    
    :Param
    :Return
    '''
    
    greetings = []
    for email in emails:
        # Extract the name from the email address (assuming it's before the "@" symbol)
        name = email.split('@')[0]
        # Split the name into first and last names (assuming a single space separates them)
        names = name.split()
        first_name = names[0] if names else ""
        last_name = names[1] if len(names) > 1 else ""

        # Generate a professional greeting
        if first_name and last_name:
            greeting = f"Dear {first_name} {last_name},"
        elif first_name:
            greeting = f"Dear {first_name},"
        else:
            greeting = "Hello,"

        greetings.append(greeting)

    return greetings

if __name__ == "__main__":
    email_list = ["john.doe@example.com", "jane.smith@example.com", "info@company.com"]
    greetings = generate_greetings(email_list)

    for email, greeting in zip(email_list, greetings):
        print(f"{greeting} Sending an email to {email}")
