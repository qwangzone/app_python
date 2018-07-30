import re

# print(re.match('(runoob)', 'www.runoob.com'))
# print(re.search('(w)', 'www.runoob.com'))
# print(re.findall('(runoob)', 'www.runoob.com,www.runoob.com,www.runoob.comwww.runoob.com,www.runoob.com,'))
# print(re.match('www', 'www.runoob.com').span())
# m = re.match('.*www.*', 'www.runoob.com')
# print(m.group(0))

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-5548532'))

re_mobilephone = re.compile(r'1(\d{10})')
print(re_mobilephone.match('28801340078'))

#匹配邮箱
def name_of_email(addr):
    re_email = re.compile(r'[a-zA-Z0-9]+@{1}[a-zA-Z0-9]+(.com)$')
    if re_email.match(addr):
        return True
    else:
        return False

#提取邮箱名称
print(name_of_email('1wqsad120@q.com'))
