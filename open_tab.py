import webbrowser
url_list_content = open('url.txt').readlines()
for url in url_list_content:
	webbrowser.open(url)