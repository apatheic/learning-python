import pyperclip, re


#find phone number
phoneRegex = re.compile(r"""(
(\d{3}|\(\d{3}\))?                  
(\s|-|\.)?                           
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)""", re.VERBOSE)

#find email
emailRegex = re.compile (r"""(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[azA-Z]{2,4})
)""", re.VERBOSE)

#search matches in text from clipboard
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copy to clipboard:')
    print('\n'.join(matches))
else:
    print('Phone numbers and Emails not found.')
