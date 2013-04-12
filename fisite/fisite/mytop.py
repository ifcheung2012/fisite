import urllib2
import top.api
import json
import datetime
import string


def getstring():
    url = "http://www.cnblogs.com"
    req = urllib2.urlopen(url)
    res = req.read()
    print res


class MyTop:
    url = ""
    port = 80
    appkey, secret = None, None

    def __init__(self, url, port, appkey, secret):
        self.url = url
        self.port = port
        self.appkey = appkey
        self.secret = secret

    '''
    cid means itmes' categoryid
    '''

    def getitemslist(self, cid, para):
        req = top.api.TaobaokeItemsGetRequest(self.url, self.port)
        req.set_app_info(top.appinfo(self.appkey, self.secret))
        req.page_no = 2
        req.page_size = 25
        req.cid = cid
        req.fields = "num_iid,title,nick,pic_url,price,click_url,shop_click_url,item_location,seller_credit_score,commission,commission_rate,commission_num,commission_volume,volume,promotion_price"
        '''
        todo :para
        '''
        import sys

        endMax = sys.maxint
        req.start_commissionRate = para["start_commissionRate"] if para["start_commissionRate"] else 0
        req.end_commissionRate = para["end_commissionNum"] if para["end_commissionNum"]    else endMax
        req.start_commissionNum = para["start_commissionNum"] if para["start_commissionNum"]  else 0
        req.end_commissionNum = para["end_commissionNum"] if para["end_commissionNum"]    else endMax
        req.start_totalnum = para["start_totalnum"] if para["start_totalnum"]       else 0
        req.end_totalnum = para["end_totalnum"] if para["end_totalnum"]         else endMax
        req.start_credit = para["start_credit"] if para["start_credit"]         else '1heart'
        req.end_credit = para["end_credit"] if para["end_credit"]           else '5goldencrown'
        req.start_price = para["start_price"] if para["start_price"]          else 0
        req.end_price = para["end_price"] if para["end_price"]            else endMax
        req.mall_item = True if para["mall_item"]            else False
        req.guarantee = True if para["guarantee"]            else False
        req.sevendays_return = True if para["sevendays_return"]     else False
        req.real_describe = True if para["real_describe"]        else False
        req.cash_coupon = True if para["cash_coupon"]          else False   #todo : when true ,http error 500,y?
        req.sort = para["sort"] if para["sort"]                 else None

        resp = req.getResponse()

        resp["taobaoke_items_get_response"]["taobaoke_items"]["total"] = 5
        respjson = resp["taobaoke_items_get_response"]["taobaoke_items"]
        res = json.dumps(respjson, indent=4, ensure_ascii=False)
        redata = string.replace(res, "taobaoke_item", "rows", 1)

        return redata


    def getitemdetail(self, num_iids):
        req = top.api.TaobaokeItemsDetailGetRequest(self.url, self.port)

        req.set_app_info(top.appinfo(appkey, secret))
        req.fields = "skus,type,seller_cid,location,prop_imgs,videos,has_discount,post_fee,ems_fee,list_time,item_imgs,click_url,shop_click_url,valid_thru,seller_credit_score,num_iid,title,nick"
        req.num_iids = num_iids
        try:
            resp = req.getResponse()
            res = json.dumps(
                resp, sort_keys=True, indent=4, ensure_ascii=False)
            print(res)
        except Exception, e:
            print(e)

    def getitemcats(self, parent_cid):
        req = top.api.ItemcatsGetRequest(self.url, self.port)

        req.set_app_info(top.appinfo(self.appkey, self.secret))
        req.fields = "cid,parent_cid,name,is_parent"
        req.parent_cid = parent_cid
        # req.cids = cids
        # req.start_credit = "1heart"

        resp = req.getResponse()
        respjson = resp["itemcats_get_response"]["item_cats"]["item_cat"]
        res = json.dumps(respjson, sort_keys=True, indent=4, ensure_ascii=False)
        return res


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
    # mytop = MyTop(url, port, appkey, secret)

    appkey2 = "21436944"
    secret2 = "48f074e58fb63330f221d2ce0ab1cf7e"

    cid = "50020808"
    parent_cid = 0
    cids = "50020808,"

    num_iid = "12348989207"
    num_iids = "12348989207"

    dt = "20130201"

    keyword = 'T'

    appkey = appkey2
    secret = secret2
    mytop = MyTop(url, port, appkey, secret)
    # print '---------------------'
    # mytop.getshops(keyword)
    # print '---------------------'
    # mytop.getdayreport(dt)
    # print '---------------------'
    #mytop.getitemdetail(num_iids)
    print '---------------------'
    # mytop.getitemslist(cid)
    print '---------------------'
    mytop.getitemcats(parent_cid)
    #parent_cid = 1801
    #mytop.getitemcats(parent_cid)
    # getstring()
