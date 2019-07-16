#coding=utf-8

import get,threading,time,requests

def Tcheck():
	global proxyTotalNum
	for i in range(0,proxyTotalNum):
		check()

def check():
	global proxyDict,proxyNum,proxyTotalNum,proxyLock
	if(proxyNum>proxyTotalNum-1):
		return
	if(proxyNum%5==0):
		print "Finished: "+str(proxyNum)+", in All: "+str(proxyTotalNum)
	checkLock.acquire()
	host = proxyDict[proxyNum]['host']
	port = proxyDict[proxyNum]['port']
	proxyNum+=1
	checkLock.release()
	if(getPage(host,port)):
		writeLock.acquire()
		f=open('px.txt','a+')
		if(f.read().find(host)!=-1):
	#		print host
			f.close()
			writeLock.release()
			return
		f.write(host+"\t"+str(port)+"\n")
		f.close()
		writeLock.release()
	else:
		return

def getPage(host,port):
	try:
		req=requests.get(url="https://www.ipip.net/",timeout=2,proxies={'https':"http://"+host+":"+str(port)})
		if(req.text.find(host)):
			return True
		else:
			return False
	except Exception,e:
		#print e
		return False

if __name__ == '__main__':
	proxyDict=get.get()
	proxyNum=0
	proxyTotalNum=len(proxyDict)
	checkLock = threading.Lock()
	writeLock = threading.Lock()
	threads=[]
	for i in range(0,5):
	#	print "A thread start"
		threads.append(threading.Thread(target=Tcheck, args= (), name = 'Thread' + str(i)))
	for t in threads:
	#	print "A thread start"
		t.setDaemon(True)
		t.start()
	#for t in threads:
	#	t.join()
	while(proxyNum<proxyTotalNum):
	#	print "Finished: "+proxyNum+", in All: "+proxyTotalNum
		time.sleep(2)
	time.sleep(2)
