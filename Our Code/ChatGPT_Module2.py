import openai

secret_key = ''
openai.api_key = secret_key
openai.api_key_path = "/Users/adamfaucher/Documents/GitHub/Auto-Email-Response-Final-Project/Our Code/key.txt"
#ChatGPT was used to generate some of this code https://chat.openai.com/
def generate_email_response(email_text, professional=True):
    '''
    A function that generates an email response, either professional or friendly.

    :Param email_text The text of the email that is being responded to
    :Param professional A boolean indicating whether to generate a professional response (True) or a friendly response (False)
    :Return The response to the given email text, in simple text
    '''
    if professional:
        prompt_type = "professional"
    else:
        prompt_type = "colloquial"

    prompt = f'Generate a {prompt_type} 5 to 8 line email body response (without a greeting or closing) to the following email, and nothing more:\n{email_text}\n\nResponse:'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    email_text = input('Paste the email text here:\n')
    is_professional = input('Is this a professional email? (yes/no): ').lower()

    if is_professional == 'yes':
        response = generate_email_response(email_text, professional=True)
    else:
        response = generate_email_response(email_text, professional=False)

    print("\nGenerated Response:")
    print(response)
