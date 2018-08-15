import requests
res = requests.get('https://www.baidu.com/')
if res.status_code == requests.codes.ok:
	print('连接成功！')
