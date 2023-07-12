import re, requests

username = "natas3"
password = "G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q"

url = 'http://'+username+'.natas.labs.overthewire.org/s3cr3t/users.txt'

auth = (username, password)
r = requests.get(url , auth=auth)
print(r.text)

print(re.findall(r'natas4:(.*)', r.text))   
