#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib2
import sys 
from lxml import etree 

urllib2_urlopen = urllib2.urlopen

def get_domain_id(username, password, domain):
	try:
		ret_xml = urllib2_urlopen('https://dnsapi.cn/Domain.List', data='login_email=' + username + '&login_password=' + password, timeout = 10).read()
		doc = etree.XML(ret_xml)
		if doc.xpath('//name/text()="' + domain + '"'):
			domain_id = doc.xpath('//id[contains(../name/text(), "' + domain + '")]/text()')
			return domain_id
		print ret_xml
		return False
	except Exception, e:
		print e
		return False

def get_record_id(username, password, domain_id, record_type="www"):
	try:
		ret_xml = urllib2_urlopen('https://dnsapi.cn/Record.List', data='login_email=' + username + '&login_password=' + password + '&domain_id=' + domain_id, timeout = 10).read()
		doc = etree.XML(ret_xml)
		if doc.xpath('//name/text()="' + record_type  + '"'):
			record_id = doc.xpath('//id[contains(../name/text(), "' + record_type + '")]/text()')
			return record_id
		return False
	except Exception, e:
		print e
		return False

def main(argc, argv):
	if 4 == argc:
		username = argv[1]
		password = argv[2]
		domain = argv[3]
		domain_id = get_domain_id(username, password, domain)[0]
		record_id = get_record_id(username, password, domain_id)[0]
		fd = open('./cfg.py', 'w')
		fd.write('un="' + username + "\"\n")
		fd.write('pw="' + password + "\"\n")
		fd.write('did=' + domain_id + "\n")
		fd.write('rid=' + record_id + "\n")
		fd.close()
	else:
		print 'Usage: python config.py login_email password domain'

if __name__ == '__main__':
	main(len(sys.argv), sys.argv)

