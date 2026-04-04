PASSWORDS = {'sashapupkin123@gmail.com': 'F7BDDubMJuxESSKHFhTxFtjVB6', 
             'blog': 'VmaLvQyKAxiVH5G8v0lifMLZf3sdt',
             'youtube': '12345'}

import sys, pyperclip
if len (sys.argv) < 2:
    print('Usage: python PasswordManager.py [Account Name] - Copy account password.')
    sys.exit

account = sys.argv[1] 
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copied to clipboard.')
else:
    print(f'There is not account named {account}.')
