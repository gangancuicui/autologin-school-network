var url = 'http://172.20.3.100/webauth.do?wlanacip=172.16.1.82&wlanacname=GXSTNU-BRAS&wlanuserip=172.17.235.41&mac=ac:75:1d:7d:ee:02&vlan=0&url=http://1.1.1.1';
var res = http.post(
        url,
        
        {
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
        'userId': , //登录账号
        'passwd': ' ',//登录密码
        }




    );
var html = res.body.string();
toast("发送Post包完毕!");