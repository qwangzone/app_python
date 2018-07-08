import itchat
"""给文件助手发信息"""
def send_wenbenzhushou():
    itchat.auto_login()
    itchat.send("hello,wangsumei",toUserName="filehelper")
"""回复发给自己的文本消息"""
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

itchat.auto_login(enableCmdQR=False)
itchat.run()