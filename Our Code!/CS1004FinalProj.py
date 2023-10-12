#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:16:54 2023

@author: adamfaucher
"""
import openai
from ChatGPT_Module.py import generate_email_response
from Closing_Module.py import generate_email_closing
from Greeting_Module.py import generate_email_greeting

# Ask the user whether the email is professional
user_input_professional = input("Is this a professional email? (yes/no): ").strip().lower()
professional = user_input_professional == 'yes'

# Example usage of the functions
user_input_name = input("Enter your name: ")
user_input_sender_name = input("Enter the sender's name: ")

email_closing = generate_email_closing(user_input_name, professional)
email_greeting = generate_email_greeting(user_input_sender_name, professional)

print("Email Closing:")
print(email_closing)

print("Email Greeting:")
print(email_greeting)

# Get user's email text
email_text = input('Paste the email text here:\n')

# Generate email response
response = generate_email_response(email_text, professional)

print("\nGenerated Response:")
print(response)
