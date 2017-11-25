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

urls = ["https://www.premproxy.com/socks-list/", 'http://www.idcloak.com/proxylist/socks-proxy-list.html']

def get_parsed_page():
    user_dir = os.environ['HOME']
    proxy_list = '%s/proxy_list' % user_dir
    if proxy_list == True:
        os.remove(proxy_list)
    sess = requests.Session()
    for url in urls:
        req = sess.get(url)
        content = req.content

        soup = BeautifulSoup(content, 'lxml')
        if url == urls[0]:
            ip_data = []
            type_data = []
            table = soup.find('table')
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')

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

        if url == urls[1]:
            port_data = []
            table = soup.find('table', id='sort')
            rows = table.find_all('tr')

            for row in rows:                     # Why are xols out of range?
                cols = row.find_all('td')
                rn = str(cols[].text.strip())
                rn1 = str(cols[].text.strip())
                rn2 = str(cols[].text.strip())
                type_data.append(rn)
                port_data.append(rn1)
                ip_data.append(r2)
                proxy_file.write('%s %s %s\n' % (rn, rn2, rn1))

    print("Gathering proxy list")
get_parsed_page()
print('list writen')
exit()
