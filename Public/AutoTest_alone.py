#coding=utf-8
import sys
import time,traceback
import os
import platform
import subprocess
import random
import re
import threading
import shutil
import hashlib
import logging
import signal



reload(sys)
sys.setdefaultencoding('utf-8')

#接口文件的根目录
home='E:\Work\Test\Enjoytherun'

#method:5个值分别为：Get,Post,Getns,Getc,Postc;
#其中Getc,Postc为跑团小程序Get\Post请求,Getns为无需签名的Get请求；
method='Getc'   

#访问接口的url地址，目前只能处理thejoyrun.com 域名的接口
#url= 'http://bet1-test.api.thejoyrun.com/user/my/mission'

url= 'https://mapp2-test.api.thejoyrun.com/wallet/getWalletByUid?timestamp=1522225709000&sid=eda1412c27f249189d4a0901d9c18c4b8&uid=32518359&appid=wx1fef2e38049c8d5f'

#Get类型的接口此项传空（即使有值也是无效的）即可，
#Post接口中所带的入参（除公共参数外），多个入参入用逗号隔开（例如a,b,c）
Interfacefields='a,b,c,d,e,f,g,h'

#测试接口模板文件地址
demopath='E:\Work\Test\Enjoytherun\Demo\Demo.txt'

#def autotestcase(home,url,method,Interfacefields,demopath):
fieldslist=list() 

##从url中获取host名
patternhost=re.compile(r'.*thejoyrun.com/')
hosta=re.search(patternhost,url,flags=0)
folder=hosta.group().replace('thejoyrun.com/','')
folder=folder.replace('http://','')
folder=folder.replace('https://','')
folder=folder.replace('-test','')
folder=folder.replace('.','')
baseurllen= len(folder)
if 'api' in folder and baseurllen>3:
	baseurl=folder.replace('api','')
	baseurl= baseurl + '_URL'
elif 'api' in folder and baseurllen<=3:
	baseurl=folder + '_URL'
else:
	baseurl=folder + '_URL'
if baseurl=='u_URL':
	baseurl='user_URL'
	
#确定接口所属的工程目录是否存在，不存在则创建，
folderdirectory = home + "\\" + folder
if os.path.exists(folderdirectory): 
	os.chdir(folderdirectory)
else:
	os.chdir(home)
	os.makedirs(folderdirectory)
	os.chdir(folderdirectory)


##从url中获取path及入参字段
getfieldstr='zzqtestauto9527'
if '?' in url:
	patternposturl=re.compile(r'thejoyrun.com/.*\?')
	postpatha=re.search(patternposturl,url,flags=0)
	postpath=postpatha.group().replace('thejoyrun.com/','')
	postpath=postpath.replace('?','')
	count1= postpath.count('/')
	count2= postpath.count('.')
	count= count1+count2
	patterngetfields=re.compile(r'\?.*$')
	getfieldsa=re.search(patterngetfields,url,flags=0)
	getfields=getfieldsa.group().replace('?','')
	getfieldlist=getfields.split('&')
	getfieldlistlen=len(getfieldlist)
	for getfield in getfieldlist:
		fieldpattern=re.compile(r'.*=')
		getfielda=re.search(fieldpattern,getfield,flags=0)
		getfieldstra=getfielda.group().replace('=','')
		getfieldstr=getfieldstr + ',' + getfieldstra
		getfieldstr=getfieldstr.replace('zzqtestauto9527,','')
		#去掉公共参数signature，timestamp
		getfieldstr=getfieldstr.replace('signature,','')	
		getfieldstr=getfieldstr.replace(',signature','')
		getfieldstr=getfieldstr.replace('signature','')		
		getfieldstr=getfieldstr.replace('timestamp,','')	
		getfieldstr=getfieldstr.replace(',timestamp','')
		getfieldstr=getfieldstr.replace('timestamp','')		
		getfieldstr=getfieldstr.replace(',,',',')
	#对跑团小程序进行特殊处理(sid,appid为公共参数)
	if folder=='mappapi':
		getfieldstr=getfieldstr.replace('sid,','')	
		getfieldstr=getfieldstr.replace(',sid','')
		getfieldstr=getfieldstr.replace('sid','')		
		getfieldstr=getfieldstr.replace(',,',',')
		getfieldstr=getfieldstr.replace('appid,','')	
		getfieldstr=getfieldstr.replace(',appid','')
		getfieldstr=getfieldstr.replace('appid','')		
		getfieldstr=getfieldstr.replace(',,',',')
	else:
		print '非小程序无需特殊处理'.decode('utf-8')
	if getfieldstr.count(',')>=1 and ',,' not in getfieldstr:
		fieldslist=getfieldstr.split(',')
		fieldslen = len(fieldslist)
		Interfacefieldstr = getfieldstr.replace(',','    ')
	elif getfieldstr.count(',')==0 and getfieldstr!='':
		fieldslist[0]=getfieldstr
		fieldslen=1
		Interfacefieldstr=getfieldstr
	else:
		fieldslen=0
		Interfacefieldstr=''		
else:
	patternposturl=re.compile(r'thejoyrun.com/.*$')
	postpatha=re.search(patternposturl,url,flags=0)
	postpath=postpatha.group().replace('thejoyrun.com/','')
	count1= postpath.count('/')
	count2= postpath.count('.')
	count= count1+count2
	##处理Interfacefields
	if len(Interfacefields)>0:
		fieldslist=Interfacefields.split(',')
		fieldslen = len(fieldslist)
		Interfacefieldstr = Interfacefields.replace(',','    ')
	else:
		fieldslen=0
		Interfacefieldstr=''
if count<=2:
	Interfacename= postpath.replace('/','_').replace('.','_')
	interfacewords= Interfacename +'_'+  method
else:
	Interfacename=postpath.partition('/')[2]
	#Interfacename=Interfacename.partition('/')[2]
	Interfacename=Interfacename.replace('/','_').replace('.','_')
	interfacewords= Interfacename +'_'+  method


	

#读取模板信息：
result = list() 
opendemo = open(demopath,'r')
demo = opendemo.readlines()
opendemo.close()
demolen = len(demo)


#判断接口用例是否存在，不存在则创建新接口文件，如存在则不创建；
if 'Get' in method:
	filename= Interfacename + '_Get.txt'
else:
	filename= Interfacename + '_Post.txt'
if os.path.exists(filename): 
	print   '此接口已存在，不需要再次创建！！'.decode('utf-8')
else:
	#处理读取的模板信息
	for  i  in range(0,demolen):
		demoline = demo[i]
		if '*** Test Cases ***' in demoline:     #处理testcase中的入参变量
			demoline = '*** Test Cases ***   '   + Interfacefieldstr + '  ret   msg'
		elif '[Arguments]' in demoline and fieldslen>0:    #处理关健字的变量，要与入参一致
			demoline = '    [Arguments]   ' 
			for fields in fieldslist:
				if fields=='':
					demoline=demoline
				else:
					demoline = demoline + '${'+ fields + '}   '
			demoline = demoline + '  ${ret}   ${msg}\n'
		elif '[Arguments]' in demoline and fieldslen==0:    #处理关健字的变量，要与入参一致
			demoline = '    [Arguments]     ${ret}   ${msg}\n' 		
		elif 'demo_Documentation' in demoline:    #处理关健字的变量，要与入参一致
			demoline = demoline.replace('demo_Documentation',postpath)	
		elif 'urlpath' in demoline:    #处理关健字的变量，要与入参一致
			demoline = demoline.replace('urlpath',postpath)	
		elif 'create dictionary' in demoline and fieldslen>0:    #处理关健字的变量，要与入参一致
			for fields2 in fieldslist:
				if fields2=='':
					demoline=demoline
				else:
					demoline = demoline  + '    set to dictionary  ${maps}  '+ fields2 + '=' + '${' + fields2 + '}'	+ '\n'			
		elif 'thejoyrun_Keywords' in demoline and method=='Post':    #处理Post公共关健字，
			demoline = demoline.replace('thejoyrun_Keywords','thejoyrun_postd')	
			demoline = demoline.replace('api_URL',baseurl)			
		elif 'thejoyrun_Keywords' in demoline and method=='Get':    #处理Get公共关健字，
			demoline = demoline.replace('thejoyrun_Keywords','thejoyrun_Getp')
			demoline = demoline.replace('api_URL',baseurl)			
		elif 'thejoyrun_Keywords' in demoline and method=='Getns':    #处理不需要签名的Get关健字，
			demoline = demoline.replace('thejoyrun_Keywords','thejoyrun_get_nosign')
			demoline = demoline.replace('api_URL',baseurl)	
		elif 'thejoyrun_Keywords' in demoline and method=='Getc':    #处理跑团小程序Get请求关健字
			demoline = demoline.replace('thejoyrun_Keywords','thejoyrun_get_crew')
			demoline = demoline.replace('api_URL',baseurl)	
		elif 'thejoyrun_Keywords' in demoline and method=='Postc':    #处理跑团小程序Post请求关健字
			demoline = demoline.replace('thejoyrun_Keywords','thejoyrun_postjson_crew')
			demoline = demoline.replace('api_URL',baseurl)			
		elif 'demo_URL' in demoline:    #处理用例关健字，
			demoline = demoline.replace('demo_URL',interfacewords)	
		elif '[Tags]' in demoline:    #标签，
			demoline = demoline.replace('Demo','Test   auto_v1')	
		elif 'api_URL' in demoline:    #接口用例的baseurl
			demoline = demoline.replace('api_URL',baseurl)			
		else:
			print  "interface is OK "
		result.append(demoline)
	creatfile=open(filename, 'w')	
	creatfile.write('%s' % ''.join(result)) 
	creatfile.close()

# '''
# if __name__ == '__main__':
    # # autotestcase(data)
    # pass

	# url= raw_input("please Enter interface url:".decode('utf-8'))
	# print "Your Interface URL is : ", url
	# Interfacefields= raw_input("Enter interface fields (multiple fields separated by commas)")
	# print "interface fields is : ", Interfacefields


	# ##从url中获取get方法的入参list()
	# patterngetfields=re.compile(r'\?.*$')
	# getfieldsa=re.search(patterngetfields,url,flags=0)
	# getfields=getfieldsa.group().replace('?','')
	# getfieldslists=getfields.split("&")
	# lenfields=len(getfieldslists)

	# ###根据输入的url信息判断使用哪个通用关健字和方法
	# if '?' in url  and 'https://mapp' in url:
		# method='crewget'

	# elif '?'  in url  and 'http://ec' in url:
		# method='Getnosign'
	# elif '?'  in url:
		# method='Getp'
	# elif '?' not in url  and 'https://mapp' in url:
		# method='crewPostjson'
	# else:
		# method='Postd'

	# ##从url中获取get方法的path参数
	# #patternGeturl=re.compile(r'thejoyrun.com/.*\?')
	# #getpatha=re.search(patternhost,url,flags=0)
	# #getpath=getpatha.group().replace('thejoyrun.com/','')
	# #getpath=getpath.replace('?','')
	# #getpathlen= len(getpath)
	# #interfacefilename= getpath.replace('/','_')
	# #interfacefilename= interfacefilename.replace('.','_')