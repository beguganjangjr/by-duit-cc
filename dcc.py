# usr/bin/python3
# Gabut gan hwhwhw
# Start: Fri May 01 2020,- 18:40:29 WIB
# Done : Fri May 01 2020,- 19:12:18 WIB
import requests as r
import re
from sys import argv
import six
from six.moves import urllib_parse, urllib_request
PY2 = six.PY2
PY3 = six.PY3
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
	html = get_.text
	if not referer:
		header.udpate({'Cookie': cookie})
	headers.update({'Origin': rurl[:-1]})
	#print(html)
	source_list = scrape_sources(html, result_blacklist, scheme, patterns, generic_patterns)
	
	print(source_list)
#	print(cookie)

def get_packed_data(html):
    packed_data = ''
    for match in re.finditer(r'(eval\s*\(function.*?)</script>', html, re.DOTALL | re.I):
        if jsunpack.detect(match.group(1)):
            packed_data += jsunpack.unpack(match.group(1))

    return packed_data

def scrape_sources(html, result_blacklist=None, scheme='http', patterns=None, generic_patterns=True):
    if patterns is None:
        patterns = []

    def __parse_to_list(_html, regex):
        _blacklist = ['.jpg', '.jpeg', '.gif', '.png', '.js', '.css', '.htm', '.html', '.php', '.srt', '.sub', '.xml', '.swf', '.vtt', '.mpd']
        _blacklist = set(_blacklist + result_blacklist)
        streams = []
        labels = []
        for r in re.finditer(regex, _html, re.DOTALL):
            match = r.groupdict()
            stream_url = match['url'].replace('&amp;', '&')
            file_name = urllib_parse.urlparse(stream_url[:-1]).path.split('/')[-1] if stream_url.endswith("/") else urllib_parse.urlparse(stream_url).path.split('/')[-1]
            label = match.get('label', file_name)
            if label is None:
                label = file_name
            blocked = not file_name or any(item in file_name.lower() for item in _blacklist) or any(item in label for item in _blacklist)
            if stream_url.startswith('//'):
                stream_url = scheme + ':' + stream_url
            if '://' not in stream_url or blocked or (stream_url in streams) or any(stream_url == t[1] for t in source_list):
                continue
            labels.append(label)
            streams.append(stream_url)

        matches = zip(labels, streams) if six.PY2 else list(zip(labels, streams))
        if matches:
            print('Scrape sources |%s| found |%s|' % (regex, matches))
        return matches

    if result_blacklist is None:
        result_blacklist = []
    elif isinstance(result_blacklist, str):
        result_blacklist = [result_blacklist]

    html = html.replace(r"\/", "/")
    html += get_packed_data(html)

    source_list = []
    if generic_patterns or not patterns:
        source_list += __parse_to_list(html, r'''["']?label\s*["']?\s*[:=]\s*["']?(?P<label>[^"',]+)["']?(?:[^}\]]+)["']?\s*file\s*["']?\s*[:=,]?\s*["'](?P<url>[^"']+)''')
        source_list += __parse_to_list(html, r'''["']?\s*(?:file|src)\s*["']?\s*[:=,]?\s*["'](?P<url>[^"']+)(?:[^}>\]]+)["']?\s*label\s*["']?\s*[:=]\s*["']?(?P<label>[^"',]+)''')
        source_list += __parse_to_list(html, r'''video[^><]+src\s*[=:]\s*['"](?P<url>[^'"]+)''')
        source_list += __parse_to_list(html, r'''source\s+src\s*=\s*['"](?P<url>[^'"]+)['"](?:.*?res\s*=\s*['"](?P<label>[^'"]+))?''')
        source_list += __parse_to_list(html, r'''["'](?:file|url)["']\s*[:=]\s*["'](?P<url>[^"']+)''')
        source_list += __parse_to_list(html, r'''param\s+name\s*=\s*"src"\s*value\s*=\s*"(?P<url>[^"]+)''')
    for regex in patterns:
        source_list += __parse_to_list(html, regex)

    source_list = list(set(source_list))

    print(source_list)
    source_list = sort_sources_list(source_list)

    return source_list

if __name__ == "__main__":
	if len(argv) < 2:
		exit(f'Jalankan : python {argv[0]} <url>')
	else:
		ByPas(argv[1])
