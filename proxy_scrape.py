#!/usr/bin/env python
"""
scrape ips and proxy type from proxy list sites
and append them to the proxychains config file
2018 

TODO;
scrape more sites

Requires python3.x, request, and BeautifulSoup

"""
#Copyright (C) 2019  HexXend
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#hexxend@protonmail.com

import requests, re 
from bs4 import BeautifulSoup
from sys import argv
import os

user_dir = os.environ['HOME']                # Use the HOME envrionment variable
list_dir = '%s/proxy_list' % user_dir
proxy_list = '%s/proxy_list/proxy_list.file' % user_dir # set where to save the list

def get_parsed_page_one():
    """
        Makes a request to the specified URL, creates a session and gets
        the page contents. 

        The contents are parsed for the table elements and the text is 
        scraped from the table elements.
    """
    url = "https://www.socks-proxy.net"

    sess = requests.Session()
    req = sess.get(url)
    content = req.content

    soup = BeautifulSoup(content, 'lxml')
    table = soup.find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')


    for row in rows:
        cols = row.find_all('td')
        try:
            rn = str(cols[0].text.strip())
            rn1 = str(cols[1].text.strip())
            rn2 = str(cols[4].text.strip()).lower()
            #rn = re.sub(':', ' ', rn)

            with open(proxy_list, 'a') as proxy_file:
                proxy_file.write('%s %s %s\n' % (rn2, rn, rn1))

        except IndexError as e:
            print('%s\nERROR: %s' % (cols, e))

def get_parsed_page_two():
    url = 'http://www.xroxy.com/free-proxy-lists/?port=&type=Socks5&ssl=&country='
    sess = requests.Session()
    req = sess.get(url)
    content = req.content
    
    soup = BeautifulSoup(content, 'lxml')
    table = soup.find('table', id='DataTables_Table_0')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    
    for row in rows:
        cols = row.find_all('td')
        rn = str(cols[0].text.strip())
        rn1 = str(cols[1].text.strip())
        rn2 = str(cols[2].text.strip()).lower()
        
        with open(proxy_list, 'a') as proxy_file:
            proxy_file.write('%s %s %s\n' % (rn2, rn, rn1))


def main():
    if  os.path.exists(proxy_list) == True:
        os.remove(proxy_list)
    
    print("Gathering proxy list")
    get_parsed_page_one()
    get_parsed_page_two()

    print('list complete')

    exit()

if __name__ == '__main__':
    main()
