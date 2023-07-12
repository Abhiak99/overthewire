from requests import *
import re

username = 'natas0'
password = 'natas0'


url = 'http://'+username+'.natas.labs.overthewire.org'

auth = (username,password)

r = get(url, auth=auth)
# print(r.text)

match = re.findall('<!--The password for natas1 is (.*) -->', r.text)
print(match[0])     
