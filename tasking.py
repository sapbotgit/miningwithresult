import requests as r
with open("code.py") as f:
  print(r.post("http://miningwithresult.sapbotcs.repl.co/task", json={"code":f.read()}).text)
input()
