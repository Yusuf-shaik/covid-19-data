import requests

def urlExists(link):
	try:
		request = requests.head(link)
		if request.status_code == 200:
	    		return True
	except:
	    return False 


def updateFailLog(url):
	f = open("failed_url.txt", "a")
	f.write(url + "\n")
	f.close()

