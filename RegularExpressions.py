'''
What is RegEx in Python?

-> RegEx stands for Regular Expression in python.
-> It's a special search pattern using which we can find and manipulate text. This text can be in the form of string or raw string.
-> It's a way to describe what kind of text we're lookin for in a bigger chunk of text.
-> For example:

'''
import re

text = 'On 2023-09-17, the conference will begin, The event will end of 2023-09-19'

# RegEx pattern to match dates defined in the format YYYY-MM-DD:
pattern = r"\d{4}-\d{2}-\d{2}"

# Finding all the matches of the date pattern in the text:
match_list = re.findall(pattern, text)
print(match_list)

'''
In-order to make regular expressions we've to follow some rules:
'''


'''
Applications of Regular Expression:

-> We mainly use RegEx for data validation such as:
  a. Mobile Number Validation: The number should contain 10 digits and it should start with 9,8,7.
  b. E-Mail Validation: These validations are performed while submitting forms.
-> Regular expressions are also used for Pattern Matching Application
-> The LIKE operator in SQL is interally implemented by using regular expression.
-> To create translators such as compiler, interpreter and assemblers. Regular expressions helps with syntax analysis and lexical analysis.
-> Data Extraction, as we can  specific information from the given data.
-> Data Cleaning: RegEx helps witj cleaning and formatting the data. We can  remove extra whitespaxe or unwanted characters.
-> Web Scraping: RegEx can be used to locate and extract specific content or information from HTML or XML documents.
  For example: You want list of URL's present on webpage.
-> Password Policies: Password policies are defined using Regular Expressions. Such as number of characters, what type of characters, how many characters in uppercase, lowercase etc.
'''



'''
In-order to perform search, the RegEx module provides a number of built-in functions. Each and every function works differently.
All of these functions are present in 're' module. So hence, we've to import 're' module at first and we've to call these function using the reference of 're' module.

(a). search()

  -> Syntax:
        re.search(pattern, data)
      Herein,
      -> pattern: The regular expression pattern that we want to search for.
      -> data: The input string in which we want to search for the pattern.
  
  -> This function will return a match object if a match is found, otherwise 'None' if no match is found.

  -> The match object will have:
      <re.Match object; span=(0, 6), match='python'>
    Herein,
      -> span represents the index positions, (i.e: starting and ending). 
      -> And the content that got matched in the given string.
  
  -> This method will return only the first match in the given string.

  -> In--order to determine what we were able to match, then by using group() method of match class we'll be able to achieve this.
  -> For Example:

  pattern = 'python'
  data = 'python is very powerful and python has a lot of features.'

  match = re.search(pattern, data)
  print(match)
  if match:
    print('Found!', match.group())
  else:
    print('Not Found!)
  

  -> For Example:
'''

pattern = 'python'
data = 'python is very powerful and python has a lot of features.'
print(re.search(pattern, data))

'''
(b). match()
(c). finditer()
(d). findall()
(e). split()
'''

'''
Flags

-> In 're' module we've some variables that we can refer to as flags which can be used as an optional argument in search function:

  a. To ignore the case while searching we can make use of 'IGNORECASE' flag.
  For Example: match = re.search(pattern, data, re.IGNORECASE)

'''