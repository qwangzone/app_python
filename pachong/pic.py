import requests,json
from bs4 import BeautifulSoup


if __name__ == '__main__':
    r = requests.get("https://unsplash.com/")
    soup = BeautifulSoup(r.text,"html.parser")
    contens=soup.find_all("img",class_="_2zEKz")
    for i in range(1, 100):
        with open("test%d.jpg"%i,'wb') as f:
            f.write(requests.get(contens[i].get('src')).content)

    # target = 'https://unsplash.com/napi/feeds/home'
    # headers = {'authorization': 'your Client-ID'}
    # req = requests.get(url=target, headers=headers, verify=False)
    # html = json.loads(req.text)
    # next_page = html['next_page']
    # print('下一页地址:', next_page)
    # for each in html['photos']:
    #     print('图片ID:', each['id'])




