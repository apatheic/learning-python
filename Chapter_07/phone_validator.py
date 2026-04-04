# its improved version my phone_extractor.py (7 chapter, Savigart)
import re, sys
print("Enter 'quit' for exit")
x = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
while True:
    try:
        inppyt=input('Enter your telephone number:  ')
        if inppyt == 'quit':
            break
        mo = x.search(inppyt)
        print(mo.group())
    except:
        print('Format for input: xxx-xxx-xxxx. Try again')
        continue
