import requests, re 

username = "natas2"
password = "h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7"

url = 'http://'+username+'.natas.labs.overthewire.org/files/users.txt'
auth = (username, password)

r = requests.get(url, auth=auth)
print(r.text)

match = re.findall(r'natas3:(.*)', r.text)
print(match[0])  
