#!/usr/bin/env python
"""
scrape ips and proxy type from proxy list sites
and append them to the proxychains config file
2017 HexXend

TODO;
scrape more sites
"""
import requests, re 
from bs4 import BeautifulSoup
from sys import argv
import os

url = "https://www.premproxy.com/socks-list/"

def get_parsed_page(url):
    user_dir = os.environ['HOME']
    proxy_list = '%s/proxy_list' % user_dir
    sess = requests.Session()
    req = sess.get(url)
    content = req.content

    soup = BeautifulSoup(content, 'lxml')
    ip_data = []
    type_data = []
    table = soup.find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    print("Gathering proxy list")

    if proxy_list == True:
        os.remove(proxy_list)

    for row in rows:
        cols = row.find_all('td')
        #cols = [x.text.strip() for x in cols]
        rn = str(cols[0].text.strip())
        rn1 = str(cols[1].text.strip())
        rn = re.sub(':', ' ', rn)
        rn1 = rn1.lower()
        ip_data.append(rn)
        type_data.append(rn1)

        with open(proxy_list, 'a') as proxy_file:
            proxy_file.write('%s %s\n' % (rn1, rn))

get_parsed_page(url)
print('list writen')
exit()
