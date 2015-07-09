# -*- coding: utf-8 -*-
from pypresent import Present
import datetime

d1 = datetime.datetime.now()
print "Start @"+str(d1)
key = "00000000000000FFFFFF".decode('hex')
print key
plain = "0000000000000000".decode('hex')
cipher = Present(key)
encrypted = cipher.encrypt(plain)
print encrypted.encode('hex')

decrypted = cipher.decrypt(encrypted)
print decrypted.encode('hex')

d2 = datetime.datetime.now()
print "Finished @"+str(d2-d1)