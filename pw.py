#! python3
#Usage: Open command line, go to file directory, type pw.py <arguement>
#ie. .../python> pw.py email 
PASSWORDS = {'email':'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345',
             'princess': 'She is too beautiful with a stinky binky'}

import sys, pyperclip
if len(sys.argv) < 2: #Makes sure that there are atleast two arguements.
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
    
account =  sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print("There is no account named " + account)
