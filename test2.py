#! /usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import codecs
import html5lib
records=[]
page=urllib2.urlopen("file:///home/thaha/Desktop/parser%20python/vitavi.php.html")
page_html=page.read()
soup=BeautifulSoup(page_html)
all_tds = [td for td in soup.findAll("table", bgcolor="#ffffff")]
fl = open('output.html', 'wb')
lol=all_tds[0]
record = '%s' % (lol)
fl.write(record)
fl.close()

