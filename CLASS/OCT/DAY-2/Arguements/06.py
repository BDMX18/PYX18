'''
Dynamic Email Formatter

Problem:
Write a function format_email(**kwargs) that constructs an email string:

Accepts any number of keyword arguments like to, cc, subject, body.

If a field is missing, use defaults: to="admin@example.com", subject="No Subject", body="".

Sample Input:

format_email(to="user@example.com", body="Welcome!")


Expected Output:

{
    'to': 'user@example.com',
    'cc': None,
    'subject': 'No Subject',
    'body': 'Welcome!'
}
'''

def format_email(to='admin@@example.com', cc=None, subject='No Subject', body='', **kwargs):
    email = {
        "to": to,
        "cc": cc,
        "subject": subject,
        "body": body
    }

    email.update(kwargs)
    return email

print(format_email(to="user@example.com", body="Welcome!"))