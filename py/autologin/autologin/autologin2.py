import requests

post_url='http://172.20.3.100/webauth.do?wlanacip=172.16.1.82&wlanacname=GXSTNU-BRAS&wlanuserip=（替换成你获取的内网ip地址）&mac=ac:75:1d:7d:ee:02&vlan=0&url=http://1.1.1.1'
data={
        'loginType': '',
        'auth_type': 0,
        'isBindMac1': 0,
        'pageid': 1,
        'templatetype': 1,
        'listbindmac':0,
        'recordmac': 0,
        'isRemind': 0,
        'url': 'http://1.1.1.1',
        'notice_pic_loop1':' /portal/uploads/pc/demo3/images/logo.jpg',
        'notice_pic_loop2': '/portal/uploads/pc/demo3/images/rrs_bg.jpg',
        'userId': ,#登录用户名
        'passwd': ' ',#登录密码
     }
reponse=requests.post(post_url,data=data)
print(reponse.status_code)
