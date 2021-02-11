#!/usr/bin/env python
# Created By ybenel

#Libraries#
try:
    from os import system as sy, path; import requests,socket,optparse
    sy("")
except ImportError:
    print(unknown2 +"Error Please Install [Requests] Module !!!")
    print(unknown6 +"Use This Command > pip install requests")
    exit(1)
# Check Internet Connection #
def cnet():
    try:
        ip = socket.gethostbyname("www.google.com")
        con = socket.create_connection((ip, 80), 2)
        return True
    except socket.error:
        pass
    return False
#Check-Email-Function#
#

def Friend(email):
    try:
        data = {"email": email}
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24'}
        response = requests.post("https://verifyemailaddress.com/result", headers=headers, data=data).text
        if "is valid" in response:
            pass
        else:
            print(email)
    except(KeyboardInterrupt,EOFError):
        print("interruptcin friend")
        exit(1)
def Main():
	try:
		with open("result.txt") as fop:
			for email in fop:
				if not email.strip() or "@" not in email: continue
				email = email.strip()
				Friend(email)
	except (KeyboardInterrupt,EOFError):
		print("interrupted ")
		exit(1)

if __name__=="__main__":
    Main()
# Done!
