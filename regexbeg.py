import re

message = 'Call me 415-555-1010 tomorrow, or at 415-555-0999'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search(message)
print(moall.list())
