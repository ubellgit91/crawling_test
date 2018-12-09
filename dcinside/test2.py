from bs4 import BeautifulSoup
from urllib import request
#
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 브라우저가 쏘는 Request의 header 부분을 고대로 재현해 준다. User-Agent로 어디에서 보낸 request인지 구분한다함.
hdr = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'image.dcinside.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
}

html = request.urlopen('http://gall.dcinside.com/board/lists/?id=comic_new1&exception_mode=recommend')
soup = BeautifulSoup(html, 'lxml')

fixed_link = "https://gall.dcinside.com"
added_link = ""

link = soup.find_all('td', {'class': 'gall_tit ub-word'})

idx = 1
# for
for m in link:
    if m.find("em", {"class": "icon_survey"}):
        pass
    elif m.find("em", {"class": "icon_notice"}):
        pass
    elif m.find("em", {"class": "icon_issue"}):
        pass
    else:
        if '번역' in m.a.text:
            print(m.a.text) # 제목 출력.
            added_link = fixed_link + m.a.get('href')
            html = request.urlopen(added_link) # 해당 게시글로 href 주소를 이용해서 접속 request.
            soup = BeautifulSoup(html, 'lxml')
            img_ul = soup.find_all("ul", {"class": "appending_file"}) # 게시글에서 업로드된 파일목록을 담고있는 ul태그를 찾음. 결과는 resultset타입으로 나옴.
            if len(img_ul) > 0: # 첨부이미지들 목록을 표시하는 ul태그가 있으면 1, 없으면 0. 즉 0이면 첨부파일이 없음.
                img_li = img_ul[0].find_all('li')
                print(img_li)
                print(type(img_li))
                for n in img_li:
                    file_name = n.a.text
                    print('filename', file_name) # li태그의 하위태그 a의 text를 가져옴.
                    file_link = n.a.get('href') # a태그의 href속성 값을 가져온다.
                    # href속성의 url주소값으로 request를 보내서 이미지를 다운로드 한다.
                    tmp_a = "http://image.dcinside.com/download.php"
                    tmp_b = "http://dcimg6.dcinside.co.kr/viewimage.php"
                    file_link2 = file_link.replace(tmp_a, tmp_b)
                    mk_req = request.Request(file_link, headers=hdr)
                    # mk_req.add_header(hdr)# url주소와 url주소로 보낼 header를 갖는 request를 만든다.
                    print(mk_req)
                    img_file = request.urlopen(mk_req) #
                    full_dir = m.a.text+"_"+n.a.text
                    # print(img_file)

                    # wb는 The wb indicates that the file is opened for writing in binary mode. jpg 파일같은 거 구성할 땐 binary mode로 써야함. 읽는건 rb
                    # 순수 텍스트는 w, 나 r로 쓴다.
                    with open(os.path.join(BASE_DIR, full_dir), 'wb') as f:
                        f.write(img_file.read())
        break





