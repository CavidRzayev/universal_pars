from bs4 import BeautifulSoup
import requests, fake_useragent
from time import sleep

# systemctl start tor.service
# pip3 install fake_useragent
# pip3 install bs4
# pip3 install requests
# pip3 install 'requests[socks]'

line = "---------------------------------------------------------------"


ipSite='http://icanhazip.com'
adress = requests.get(ipSite)

print(line + "\n[*] Sizin IP adress:\n"+adress.text + line)
print("[!] Tor networka qosulur /", end = "")

for _ in range(5):
	sleep(0.2); print(end = '.', flush = True)

proxie = {
	'http': 'socks5h://127.0.0.1:9050', 
	'https': 'socks5h://127.0.0.1:9050'
}

try:
	adress = requests.get(ipSite, proxies = proxie, headers = header)
	
except:
	connection = False
	print("/\n[x] Tor networka qoshulma diyandirildi k\n" + line)
	
else:
	connection = True
	print("/\n[+] Tora qosuldu \n" + line)
	print("[*] Sizin Tor IP adress:\n" + adress.text + line)

finally:
	url = input("[!] Url qey edin :\nhttp://")

	if connection == True:
		page = requests.get("http://"+url.split()[0], proxies = proxie)
	else:
		page = requests.get("http://"+url.split()[0])

	soup = BeautifulSoup(page.text, "html.parser")

	if url.split()[0] == url.split()[-1]:
		with open("index.html","w") as html:
			for tag in soup.findAll('html'):
				html.write(str(tag))
			print(line,"\nFile: 'index.html' yaradildi")
	else:
		if url.split()[1] == url.split()[-1]:
			for tag in soup.findAll(url.split()[1]):
				print(tag)
		else:
			if url.split()[2] == "inside":
				for tag in soup.findAll(url.split()[1]):
					print(tag.text)
			else:
				for tag in soup.findAll(url.split()[1]):
					print(tag[url.split()[2]])
	print(line)
