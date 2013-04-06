__author__ = 'ifcheung'
# -*- coding:utf-8 -*-
import urllib,urllib2
import os,Queue,random,sys
from urllib import FancyURLopener
class MyOpener(FancyURLopener):
    version='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'

class Spider:
    def get_html(self,url):
        myopener = MyOpener()
        sock = myopener.open(url)
        htmlSource = sock.read()
        sock.close()
        return htmlSource
    def analysis_html(self,htmlSource):
        import xml.html.soupparser as soupparser
        dom = soupparser.fromstring(htmlSource)
        Url=dom.xpath('//*[@id="RecentBlogs"]/ul[1]/li/div/h3/a[@href]')
        title=dom.xpath('//*[@id="RecentBlogs"]/ul[1]/li/div/h3/a/text()')
        writer=dom.xpath('//*[@id="RecentBlogs"]/ul[1]/li/div/div/text()')
        for i in  range(len(title)):
            print title[i].encode('utf-8'),Url[i].get('href').encode('utf-8'),writer[i].encode('utf-8')
if __name__ == '__main__':
    spider = Spider()
    url=['http://www.oschina.net/blog/more?p=%s#' %(i) for i in range(10)]
    urls=Queue.Queue()
    for i in url:
        urls.put(i)
    for i in range(urls.qsize()):
        url=urls.get()
        htmlSource = spider.get_html(url)
        spider.analysis_html(htmlSource)