# autologin-school-network 广科师校园网自动登录

## 前言
    新学期到了，校园网的认证方式也改成了网页认证的形式😓，嫌每天都要去网页登录太麻烦了，所以写了这一个自动登录的脚本。

## Python
    连上网络以后点击dist里的exe文件就可以自动发送Post请求包来自动登录了，发送前要把py文件内的账号和密码换成自己的，可以用文本编辑器编辑。仅支持64位window系统，32位的请自行安装python环境来编译运行。
``` 
    post_url='http://172.20.3.100/webauth.do?wlanacip=172.16.1.82&wlanacname=GXSTNU-BRAS&wlanuserip=（替换成你获取的内网ip地址）&mac=ac:75:1d:7d:ee:02&vlan=0&url=http://1.1.1.1'
    
    'userId' : 账号,      #登录用户名
    'passwd' : ' 密码 ',  #登录密码
    
```
## autojs
    此脚本可以在安卓设备上运行，安装两个apk包以后将js文件导入进去，修改账号密码就可以了，也可以设置定时运行。
```
    var url = 'http://172.20.3.100/webauth.do?wlanacip=172.16.1.82&wlanacname=GXSTNU-BRAS&wlanuserip=（替换成你获取的内网ip地址）&mac=ac:75:1d:7d:ee:02&vlan=0&url=http://1.1.1.1';
    
    'userId': 账号 , //登录账号
    'passwd': ' 密码 ',//登录密码
```
## 最后
    Enjoy it！有帮助的话麻烦帮我点一下星标😋
