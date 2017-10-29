#encoding=utf-8

proxyUrl='http://tvp.daxiangdaili.com/ip/?'

#此处修改为你的订单号码
proxyBill='Your Billing Number'

#一次提取的数量
proxyNum=20

proxyFormat='json'

#proxyProtocol='https'

def getUrl():
	global proxyUrl
	proxyUrl+='tid='
	proxyUrl+=proxyBill
	proxyUrl+='&num='
	proxyUrl+=str(proxyNum)
	proxyUrl+='&format='
	proxyUrl+=proxyFormat
	proxyUrl+='&protocol='
	proxyUrl+=proxyProtocol
	return proxyUrl
