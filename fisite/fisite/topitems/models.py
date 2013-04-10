__author__ = 'ifcheung'

from django.db import models

class TbkTpItemManager(models.Manager):
    def ItemCount(self,keyword):
        return self.filter(title__icontains=keyword).count()
class TbkTpItemCat(models.Model):
    name   = models.CharField(max_length=50)
    tags   = models.CharField(max_length=50)
    pid    = models.IntegerField()
    img    = models.URLField()
    addtime = models.DateTimeField()

class TbkTpItem(models.Model):
    key_id = models.CharField(max_length=50)
    title  = models.CharField(max_length=255)
    intro  = models.CharField(max_length=255)
    imgurl = models.URLField()
    price  = models.DecimalField(max_digits=5, decimal_places=2)
    cmsrates = models.FloatField(max_length=100)
    clickurl = models.URLField()
    #catid    = models.ForeignKey(TbkTpItemCat)
    addtime  = models.DateTimeField()
    status   = models.IntegerField()

    objects  = TbkTpItemManager()
    def __unicode__(self):
        return self.title

