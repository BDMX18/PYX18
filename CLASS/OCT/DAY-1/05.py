'''
Question: Functional Email Validator

Write a function validate_emails(emails) that:

Takes a list of email strings emails.

Uses functional programming tools (filter, map, lambda, etc.) to:

Filter out invalid emails.

An email is valid if:

It contains exactly one '@' character.

The domain part (after '@') contains at least one '.'.

The username part (before '@') is non-empty.

Returns a list of valid emails in lowercase.

Example:
input_emails = ['User@example.com', 'invalid-email', 'john.doe@company', 'jane@company.com']

print(validate_emails(input_emails))


Expected output:

['user@example.com', 'jane@company.com']
'''

def validate_email(email_list):
  first_validation = list(filter(lambda mail: mail.count('@') == 1, email_list))
  second_validation = list(filter(lambda mail: '.' in mail[mail.index('@')+1:], first_validation))
  third_validation = list(filter(lambda mail: mail[:mail.index('@')] != '', second_validation))
  valid_mails = list(map(lambda mail: mail.lower(), third_validation))
  return valid_mails

num = int(input('Number Of E-Mails You Want To Add: '))
email_list = [input(f'Enter Mail {i+1}: ') for i in range(num)]
print(validate_email(email_list))