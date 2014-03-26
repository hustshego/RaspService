#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shiningchan
# @Date:   2014-01-23 16:41:14
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-03-26 19:25:44

import urllib
import urllib2


HOST_URL = "http://127.0.0.1:8080/service/"

def post(url, data):
	req = urllib2.Request(url)
	data = urllib.urlencode(data)
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	response = opener.open(req, data)
	return response.read()

def get(url, data):
	data = urllib.urlencode(data)
	full_url = url + '?' + data
	response = urllib.urlopen(full_url)
	return response.read()

def registerTest():
	posturl = HOST_URL + "register"
	data = {'nick':'testUser','password':'123456'}
	print post(posturl, data)

def loginTest():
	posturl = "http://127.0.0.1:8080/service/login"
	data = {'user_id':'1','nick':'testUser','password':'123456'}
	print post(posturl, data)

def addTaskTest(user_id,switch_id):
	posturl = "http://127.0.0.1:8080/service/addTask"


	if_expression = {"temperature":"20-30","humidity":"12,17"}
	data = {'user_id':user_id,'switch_id':switch_id,'target_status':'1','if_expression':if_expression}
	print post(posturl, data)

def addSwitchTest(name,level):
	posturl = "http://127.0.0.1:8080/service/addSwitch"
	data = {'name':name,'level':level}
	print post(posturl, data)

def delSwitchTest():
	posturl = HOST_URL+ "delSwitch"
	data = {'switch_id':'2'}
	print post(posturl, data)

def getSwitchTest(page):
	posturl = "http://127.0.0.1:8080/service/getSwitch"
	data = {'page':page}
	print get(posturl, data)

def changeSwitchStatusTest(switch_id,status):
	posturl = "http://127.0.0.1:8080/service/changeSwitchStatus"
	data = {'switch_id':switch_id,'status':status}
	print post(posturl, data)

if __name__ == '__main__':
	#registerTest()
	#loginTest()
	#addTaskTest()
	#delSwitchTest()
	#for integer in range(10):
		#addSwitchTest("switch"+str(integer),"0")
	#etSwitchTest(1)
	#for integer in range(10):
		#addTaskTest("1",str(integer+1))
	#changeSwitchStatusTest("3","1");

	pass