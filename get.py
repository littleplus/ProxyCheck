#coding=utf-8

import config,json,requests

def get():
	try:
		proxyJson=requests.get(url=config.getUrl(),timeout=5)
		proxyDict=json.loads(proxyJson.text)
		return proxyDict
	except Exception,e:
		print(e)
		return
