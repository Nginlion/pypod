pypod
=====

基于Python的动态域名解析脚本。

修改自[DNSPod官方脚本][0]，感谢[Li Chuangbo][1]的工作！

主要修改了获取外网IP的方式，通过[ip138提供的方法][2]获取IP。目前在树莓派上运行正常。

配置方式目前请按照如下步骤：

1. 首先请在dnspod上新建一条www的A记录；
2. 在本地先执行config.py脚本，执行方法是：
<pre>
python config.py your_dnspod_username your_dnspod_password domain 
</pre>
3. 之后执行pypod脚本
<pre>
python pypod.py
</pre>

[0]: https://gist.github.com/chuangbo/833369
[1]: https://github.com/chuangbo
[2]: http://iframe.ip138.com/ic.asp
