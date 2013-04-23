#-*- encoding=UTF-8 -*-
__author__ = 'ifcheung'

from django.contrib import admin
from fisite.topitems.models import TbkTpItem, TbkTpItemCat




class TbkTpItemAdmin(admin.ModelAdmin):
    list_display = ('key_id', 'get_catname', 'get_img', 'title', 'intro', 'price', 'cmsrates', 'addtime', 'status')
    list_filter = ('addtime', 'catid', 'status')
    list_display_links = ('title',)


    def get_catname(self, tbktpitem):
        return tbktpitem.catid.name
    get_catname.allow_tags = True
    get_catname.short_description = 'category(s)'

    def get_img(self, tbktpitem):
        imgurl = tbktpitem.imgurl
        return '<img src=' + imgurl + ' width = 200 height=150 />'
    get_img.allow_tags = True
    get_img.short_description = 'imgs'


class TbkTpItemCatAdmin(admin.ModelAdmin):
    list_display = ('cid', 'pid', 'name', 'tags', 'img', 'addtime')


admin.site.register(TbkTpItemCat, TbkTpItemCatAdmin)
admin.site.register(TbkTpItem, TbkTpItemAdmin)