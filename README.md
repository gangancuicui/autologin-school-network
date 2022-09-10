# autologin-school-network 广科师校园网自动登录

## 前言
    新学期到了，校园网的认证方式也改成了网页认证的形式😓，嫌每天都要去网页登录太麻烦了，所以写了这一个自动登录的脚本。

## Python
    连上网络以后点击dist里的exe文件就可以自动发送Post请求包来自动登录了，发送前要把py文件内的账号和密码换成自己的，可以用文本编辑器编辑。仅支持64位window系统，32位的请自行安装python环境来编译运行。
``` 
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
    
```
## autojs
    此脚本可以在安卓设备上运行，安装两个apk包以后将js文件导入进去，修改账号密码就可以了，也可以设置定时运行。
```
var url = 'http://172.20.3.100/webauth.do?wlanacip=172.16.1.82&wlanacname=GXSTNU-BRAS&wlanuserip=（替换成你获取的内网ip地址）&mac=ac:75:1d:7d:ee:02&vlan=0&url=http://1.1.1.1';
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
```
## 最后
    Enjoy it！有帮助的话麻烦帮我点一下星标😋
