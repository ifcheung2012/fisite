
import urllib2
import top.api
import json
import datetime


def getstring():
    url = "http://www.cnblogs.com"
    req = urllib2.urlopen(url)
    res = req.read()
    print res


class toptest:
    url = ""
    port = 80
    appkey, secret = None, None

    def __init__(self, url, port, appkey, secret):
        self.url = url
        self.port = port
        self.appkey = appkey
        self.secret = secret

    def getitemslist(self, cid):

        req = top.api.TaobaokeItemsGetRequest(self.url, self.port)
        req.set_app_info(top.appinfo(self.appkey, self.secret))
        req.page_no = 2
        req.page_size = 2
        req.cid = cid
        req.fields = "num_iid,title,nick,pic_url,price,click_url,shop_click_url,item_location,seller_credit_score,commission_rate,commision,promotion_price"
        resp = req.getResponse()
        res = json.dumps(resp, sort_keys=True, indent=4, ensure_ascii=False)
        print res
        # print 'DATA:', repr(resp)
        # print 'repr(data)          :', len(repr(resp))
        # print 'dumps(data)         :', len(json.dumps(resp))
        # print 'dumps(data,indent=2) :', len(json.dumps(resp, indent=4))
        # print 'dumps(resp,separators):', len(json.dumps(resp, separators=(',',
        # ':')))

    def getitemdetail(self, num_iids):
        req = top.api.TaobaokeItemsDetailGetRequest(url, port)
        req.set_app_info(top.appinfo(appkey, secret))
        req.fields = "click_url,shop_click_url,seller_credit_score,num_iid,title,nick"
        req.num_iids = num_iids
        try:
            resp = req.getResponse()
            res = json.dumps(
                resp, sort_keys=True, indent=4, ensure_ascii=False)
            print(res)
        except Exception, e:
            print(e)

    def getitemcats(self, cids, parent_cid):
        req = top.api.ItemcatsGetRequest(url, port)
        req.set_app_info(top.appinfo(appkey, secret))
        req.fields = "cid,parent_cid,name,is_parent"
        req.parent_cid = parent_cid
        req.cids = cids
        req.start_credit = "1heart"
        try:
            resp = req.getResponse()
            res = json.dumps(
                resp, sort_keys=True, indent=4, ensure_ascii=False)
            print(res)
        except Exception, e:
            print(e)

    def getdayreport(self, dt):
        req = top.api.TaobaokeReportGetRequest(url, port)
        req.set_app_info(top.appinfo(appkey, secret))
        req.fields = "trade_id,pay_time,pay_price,num_iid,outer_code,commission_rate,commission,seller_nick,pay_time,app_key"
        req.date = dt
        try:
            resp = req.getResponse()
            res = json.dumps(
                resp, sort_keys=True, indent=4, ensure_ascii=False)
            print(res)
        except Exception, e:
            print(e)

    def getshops(self, keyword):
        req = top.api.TaobaokeShopsGetRequest(url, port)
        req.set_app_info(top.appinfo(appkey, secret))
        req.fields = "click_url,shop_title,seller_credit,shop_type"
        req.keyword = keyword
        try:
            resp = req.getResponse()
            res = json.dumps(
                resp, sort_keys=True, indent=4, ensure_ascii=False)
            print(res)
        except Exception, e:
            print(e)

if __name__ == "__main__":

    url = "gw.api.taobao.com"
    port = 80
    appkey1 = "21430097"
    secret1 = "b905348541f429bcb9215cf804f7df72"

    appkey2 = "21436944"
    secret2 = "48f074e58fb63330f221d2ce0ab1cf7e"

    cid = 50020808
    parent_cid = 50020808
    cids = "50020808,"

    num_iid = "1500009887333"
    num_iids = "15684538297"

    dt = "20130201"

    keyword = 'T'

    appkey = appkey2
    secret = secret2
    mytop = toptest(url, port, appkey, secret)
    print '---------------------'
    mytop.getshops(keyword)
    print '---------------------'
    mytop.getdayreport(dt)
    print '---------------------'
    mytop.getitemdetail(num_iids)
    print '---------------------'
    mytop.getitemslist(cid)
    print '---------------------'
    mytop.getitemcats(cids, parent_cid)
    # getstring()
