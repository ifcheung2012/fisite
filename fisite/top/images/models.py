from django.db import models

# Create your models here.
class ImageUp(models.Model):
    img_name = models.CharField(max_length=100)
    imgurl = models.URLField(verify_exists=False, max_length=200)
    imgsize = models.IntegerField()
    uptime = models.DateTimeField(auto_now_add=True, auto_now=True)
    upuserid = models.IntegerField()
    upposition = models.CharField(max_length=50 )
    def __unicode__(self):
        return self.img_name

class ImageTline(models.Model):
    imgname = models.CharField(max_length=50)
    imgurl = models.URLField(verify_exists=False, max_length=200)
    imgsize = models.IntegerField()
    savetime = models.DateTimeField(auto_now_add=True, auto_now=True)
    saveuserid = models.IntegerField()
    saveposition = models.CharField(max_length=50)
    def __unicode__(self):
        return self.imgname

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True,null=True)
    content = models.TextField(blank=True)
    creatime = models.DateTimeField(auto_now_add=True, auto_now=True, blank=True, null=True)
    userid = models.IntegerField()
    lastupdatime = models.DateTimeField(auto_now_add=True, auto_now=True, blank=True, null=True)
    def __unicode__(self):
        return self.title



