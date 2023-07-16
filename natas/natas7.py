import requests, re
from bs4 import BeautifulSoup

username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'

url = 'http://'+username+'.natas.labs.overthewire.org/'
auth =(username, password)
secret = "FOEIUWGHFEEUHOFUOIU"
data = {"secret" : secret , "submit" : "submit"}
r = requests.post(url,data = data, auth=auth)
print(r.headers)
print(r.text)

# print(BeautifulSoup(r.text, "html.parser").text)

print(re.findall(r'natas7 is (.*)', r.text))
