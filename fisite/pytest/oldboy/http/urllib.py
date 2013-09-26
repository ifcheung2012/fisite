# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib

url ='http://127.0.0.1:8000/admin/'
bodyfieleds = {'username':'ifcheung','password':'xpendif'}
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
req = urllib2.Request(url, urllib.urlencode(bodyfieleds))
resp = opener.open(req, timeout=60)

strlist = resp.read()