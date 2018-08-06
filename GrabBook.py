from selenium import webdriver
dr = webdriver.Chrome()
dr.maximize_window()
dr.get("http://www.xinshubao.net/14/14506/")
eles = dr.find_elements_by_css_selector("._chapter>li")
print(len(eles))
section_name = []
#print(eles[0].find_element_by_tag_name("a").get_attribute("href"))
for i in eles:
    section_name.append(i.find_element_by_tag_name("a").get_attribute("href"))
print(section_name[0])
with open("test.txt",'a+') as f:
    for i in section_name:
        dr.get(i)
        content1 = dr.find_element_by_id("content").text
        dr.find_element_by_css_selector("div.bottem1>p:nth-child(2)>a:nth-child(4)").click()
        content2 = dr.find_element_by_id("content").text
        f.write(content1)
        f.write(content2)

# a = "Wqwqwqwq sasa "
# print(a.count("sa"))
# dr.get("http://www.xinshubao.net/14/14506/1319763.html")
# #a=dr.find_element_by_id("content").get_attribute("innerHTML")
# a=dr.find_element_by_id("content").text
# print(a)
# dr.find_element_by_css_selector("div.bottem1>p:nth-child(2)>a:nth-child(4)").click()
# a="http://www.xinshubao.net/14/14506/1319763.html"
# b = a.replace("http://www.xinshubao.net/14/14506/1319763.html","http://www.xinshubao.net/14/14506/1319763_2.html")
# print(a)
# print(b)
