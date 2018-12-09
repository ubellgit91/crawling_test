from bs4 import BeautifulSoup
from urllib import request

html = request.urlopen('http://gall.dcinside.com/board/lists?id=comic_new1&exception_mode=recommend')
soup = BeautifulSoup(html, 'lxml')

print (soup)
print ('---'*3)
# 기준
link = soup.find_all("td",{"class": "gall_tit ub-word"})

for m in link:
    if m.find("em",{"class":"icon_survey"}):
        pass
    elif m.find("em",{"class":"icon_notice"}):
        pass
    else:
        print(m.a.text)