# -*- coding: utf-8 -*-
import top.api

url = "gw.api.taobao.com"
port=80
appkey="21430097"
secret ="b905348541f429bcb9215cf804f7df72"

req=top.api.TaobaokeItemsGetRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))

req.fields="num_iid,title,nick,pic_url,price,click_url,commission,commission_rate,commission_num,commission_volume,shop_click_url,seller_credit_score,item_location,volume"
try:
        resp= req.getResponse()
        print(resp)
except Exception,e:
        print(e)
