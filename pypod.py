#!/usr/bin/env python
#-*- coding:utf-8 -*-

import httplib, urllib, urllib2
import socket
import time
import re
import cfg

urllib2_urlopen = urllib2.urlopen
re_findall = re.findall

params = dict(
    login_email=cfg.un, # replace with your email
    login_password=cfg.pw, # replace with your password
    format="json",
    domain_id=cfg.did, # replace with your domain_od, can get it by API Domain.List
    record_id=cfg.rid, # replace with your record_id, can get it by API Record.List
    sub_domain="www", # replace with your sub_domain
    record_line="默认",
)
current_ip = None

def ddns(ip):
    params.update(dict(value=ip))
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Record.Ddns", urllib.urlencode(params), headers)
    
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()
    return response.status == 200

def getip():
	try:
		ip = re_findall(r"\[.+\]", urllib2_urlopen("http://iframe.ip138.com/ic.asp", timeout=10).read())[0][1:-1]
	except Exception, e:
		print e
		pass
	return ip

if __name__ == '__main__':
    while True:
        try:
            ip = getip()
            print ip
            if current_ip != ip:
                if ddns(ip):
                    current_ip = ip
        except Exception, e:
            print e
            pass
        time.sleep(300)
