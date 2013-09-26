def getinfo(username,password,routipinfo):
    import httplib,re,base64
    conn = httplib.HTTPConnection(routipinfo)
    headers = {"User-Agent": "python host",
               # "Referer":"http://192.168.1.1:8080/status-devices.asp",
               # "Host":"192.168.1.1:8080",
               "Content-type":"application/x-www-form-urlencoded",
               "Authorization":"Basic %s" % base64.encodestring('%s:%s' % (username,password))[:-1],
               "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
               "Accept-Encoding":"gzip,deflate",
               "Connection": "keep-alive"}
    conn.request("GET","","",headers)
    response =conn.getresponse()
    reinfo = response.read()

    response.close()
    conn.close()
    print base64.encodestring('%s:%s' % (username,password))[:-1]

    keyword = re.search('',reinfo)
    print reinfo


if __name__ == "__main__":
    getinfo("root","xpendif","192.168.1.1:8080")