from ChatGPT_Module2 import generate_email_response
from Greeting_Practice import generate_email_greeting
from Greeting_Practice import is_professional
from Closing_Module import generate_email_closing

#ChatGPT was used to generate some of this code https://chat.openai.com/

# Creating the greeting of the email
input_sender_name = input("Enter the sender's name: ")
professional = is_professional(input_sender_name)
email_greeting = generate_email_greeting(input_sender_name, professional)[0]
print("Email Greeting:", email_greeting,"\n")

# Creating the closing of the email
input_user_name = input("Enter your name: ")
email_closing = generate_email_closing(input_user_name, professional)
print("Email Closing:", email_closing, '\n')

# Get user's email text
email_text = input('Paste the email text here:')

# Generate email response
response = generate_email_response(email_text, professional)

print("Generated Response:", response)
print('\nFull response:\n\n', email_greeting, '\n', response, '\n', email_closing)
