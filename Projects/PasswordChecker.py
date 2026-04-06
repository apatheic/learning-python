import re

def passwordCheck(password):
    if len(password) < 8:
        return False
    if re.search('[A-Z]', password) is None:
        return False
    if re.search('[a-z]', password) is None:
        return False
    if re.search(r'\d', password) is None:
        return False
    return True

user_password=input('Input your password:\n\t')
if passwordCheck(user_password) == True:
    print('Your passwd is good')
else:
    print('You doesnt OPSEC')
