from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException

list = ""
catr = "PROXYLIST_DOWNLOAD_HTTP"
scrapper = Scrapper(category=catr, print_err_trace=False)
data = scrapper.getProxies()
for item in data.proxies:
	proxyline = 'http://{}:{}\n'.format(item.ip, item.port)
	list += proxyline
with open("proxy.txt", "w") as f:
	f.write(list)
