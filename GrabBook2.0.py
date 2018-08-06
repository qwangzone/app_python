from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':
    url = "http://www.xinshubao.net/14/14506/"
    r_title = requests.get(url)
    soup = BeautifulSoup(r_title.text,"html.parser")
    eles = soup.find("ul",class_="_chapter").find_all("li")
    print(len(eles))
    section_name = []
    for i in eles:
        section_name.append(i.find("a").get("href").split("/14506/")[1])
    #print(section_name[0])
    # for i in section_name:
    #     r_content = requests.get(url+i).text
    #     sop = BeautifulSoup(r_content,"html.parser")
    #     text = sop.find("id=content").get_text()
    html_doc = requests.get(url + section_name[0]).text
    sop = BeautifulSoup(html_doc,"html.parser")

    content = sop.find("div",id="content").get_text()
    print(content)