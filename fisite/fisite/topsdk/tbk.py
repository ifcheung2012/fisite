import top.api

url = "http://gw.api.tbsandbox.com/router/rest?sign=494C9C98451DBE31CC3AF23E9DBB727A&timestamp=2013-03-20+19%3A34%3A21&v=2.0&app_key=1012129701&method=taobao.taobaoke.items.get&partner_id=top-apitools&format=json&fields=num_iid,title,nick,pic_url,price,click_url,commission,commission_rate,commission_num,commission_volume,shop_click_url,seller_credit_score,item_location,volume"
port=80
appkey = "1012129701"
secret = ""
req=top.api.TaobaokeItemsGetRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))

req.fields="num_iid,title,nick,pic_url,price,click_url,commission,commission_rate,commission_num,commission_volume,shop_click_url,seller_credit_score,item_location,volume"
kry:
    resp= req.getResponse()
    print(resp)
except Exception,e:
    print(e)


