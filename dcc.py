# usr/bin/python3
# Gabut gan hwhwhw
# Start: Fri May 01 2020,- 18:40:29 WIB
# Done : Fri May 01 2020,- 19:12:18 WIB
import requests as r
import re
from sys import argv
from six.moves import urllib_parse, urllib_request
def ByPas(url, referer=True):
	print('\n[÷] Bypasing => '+url)
	result_blacklist = []
	result_blacklist = list(set(result_blacklist + ['.smil']))

	scheme = urllib_parse.urlparse(url).scheme
	generic_patterns=False
	u = urllib_parse.urlparse(url)
	patterns=[r'''(?:mp4|hls)":\s*"(?P<url>[^"]+)",\s*"video_height":\s*(?P<label>[^,]+)''']
	rurl = '{0}://{1}/'.format(u.scheme, u.netloc)
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
	if referer:
		headers.update({'Referer': rurl})
	get_ = r.get(url, headers=headers)
	response_headers = get_.headers
	cookie = response_headers.get('Set-Cookie', None)
	print(cookie)
	if cookie:
		headers.update({'Cookie': cookie})
	cookies = cookie
	html = r.get(url, cookies=cookies).text
	if not referer:
		header.udpate({'Cookie': cookie})
	headers.update({'Origin': rurl[:-1]})
	#print(html)
	source_list = scrape_sources(html, result_blacklist, scheme, patterns, generic_patterns)
	
	print(source_list)
#	print(cookie)
def scrape_sources(html, result_blacklist=None, scheme='http', patterns=None, generic_patterns=True):
    if patterns is None:
        patterns = []
if __name__ == "__main__":
	if len(argv) < 2:
		exit(f'Jalankan : python {argv[0]} <url>')
	else:
		ByPas(argv[1])
