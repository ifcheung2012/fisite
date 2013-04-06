# -*- coding: utf-8 -*-
import top.api

url = "gw.api.taobao.com"
port = 80
appkey = "21430097"
secret = "b905348541f429bcb9215cf804f7df72"

req = top.api.TaobaokeItemsGetRequest(url, port)
req.set_app_info(top.appinfo(appkey, secret))

req.fields = "num_iid,title,nick,pic_url,price,click_url,commission,commission_rate,commission_num,commission_volume,shop_click_url,seller_credit_score,item_location,volume"
req.Nick = "jay"
req.Pid = 123456L
req.Keyword = "abc"
req.Cid = 123L
req.StartPrice = "1"
req.EndPrice = "999"
req.AutoSend = "true"
req.Area = "杭州"
req.StartCredit = "1heart"
req.EndCredit = "1heart"
req.Sort = "price_desc"
req.Guarantee = "true"
req.StartCommissionRate = "1234"
req.EndCommissionRate = "2345"
req.StartCommissionNum = "1000"
req.EndCommissionNum = "10000"
req.StartTotalnum = "1"
req.EndTotalnum = "10"
req.CashCoupon = "true"
req.VipCard = "true"
req.OverseasItem = "true"
req.SevendaysReturn = "true"
req.RealDescribe = "true"
req.OnemonthRepair = "true"
req.CashOndelivery = "true"
req.MallItem = "true"
req.PageNo = 1L
req.PageSize = 40L
req.OuterCode = "abc"
req.IsMobile = True
try:
        resp = req.getResponse()
        print(resp)
except Exception, e:
        print(e)
