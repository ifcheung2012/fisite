'''
Created by auto_sdk on 2013-03-20 16:37:20
'''
from top.api.base import RestApi
class ShoprecommendItemsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.count = None
		self.ext = None
		self.recommend_type = None
		self.seller_id = None

	def getapiname(self):
		return 'taobao.shoprecommend.items.get'
