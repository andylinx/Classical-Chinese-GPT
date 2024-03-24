import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
}
response=requests.get("http://www.360doc.com/content/21/0429/10/682382_974705991.shtml",headers=headers)
if response.ok:
    print("ok")
soup=BeautifulSoup(response.text,"html.parser")
all_word=soup.findAll("section")
with open('output.txt', 'w') as file:
    for word in all_word:
        print(word.get_text())
        file.write(word.get_text()+'\n')
        