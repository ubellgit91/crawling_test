from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request
#


url = "http://gall.dcinside.com/board/lists?id=comic_new1&exception_mode=recommend"
hdr = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'gall.dcinside.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
}

# 클래스 형태로 크롤러를 만들어 보자.
class DcCrawler(BeautifulSoup):
    def __init__(self, url, parser, **headers): # 헤더가 필요하면
        self.req = request.Request(url, headers=headers)
        self.res = request.urlopen(self.req)
        super().__init__(self.res, parser)


if __name__=='__main__':
    crawler = DcCrawler(url, 'lxml')
    result = crawler.find_all('td', {'class': 'gall_tit ub-word'})

    for m in result:
        if m.find("em", {"class": "icon_survey"}):
            pass
        elif m.find("em", {"class": "icon_notice"}):
            pass
        elif m.find("em", {"class": "icon_issue"}):
            pass
        else:
            if '번역' in m.a.text:
                print(m.a.text)