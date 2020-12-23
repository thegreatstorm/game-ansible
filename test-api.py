import requests

username = input("Input your github username: ")
password = input("Input your github pass/token: ")


r = requests.get('https://api.github.com/repos/thegreatstorm/raging-automation/contents/rustserver/test.yml?ref=main', auth=(username, password))
print(r.status_code)