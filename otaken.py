from socialscan.util import Platforms, sync_execute_queries
import time

with open("proxy.txt") as prox:    proxies = [i.strip() for i in prox.readlines()]
with open("input.txt") as f:    content = [i.strip() for i in f.readlines()]
email = content
proxy = proxies
emailList = []
apps = [Platforms.INSTAGRAM]
results = sync_execute_queries(email, apps, proxy)
for result in results:
	try:
		if not result.available:
			print(result.query)
			emailList.append(result.query)
			with open("output.txt", "w") as f2:
				for ele in emailList:
					f2.write(ele + '\n')
		else:
			pass

	except KeyboardInterrupt:
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
