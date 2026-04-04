#My first expiriense with regular (Chapter 7, Savigart

import re
x = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = x.search('mynumis111-111-1111')
print(mo.group(2))
