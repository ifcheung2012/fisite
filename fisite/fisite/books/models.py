from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    website =  models.URLField()
    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField('e-mail',blank=True)
    def __unicode__(self):
        return self.first_name

class BookManager(models.Manager):
    def titlecount(self,keyword):
        return self.filter(title__icontains=keyword).count()

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date=models.DateField()
    objects=BookManager()
    def __unicode__(self):
        return self.title
