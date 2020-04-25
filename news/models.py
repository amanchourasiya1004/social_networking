from django.db import models

# Create your models here.
class News(models.Model):
    name = models.TextField(default='-')
    short_txt = models.TextField(default='-') 
    body_txt = models.TextField(default='-')
    date = models.CharField(max_length=12, default='-')
    pic = models.CharField(max_length=20, default='-')
    writer = models.CharField(max_length=30, default='-')
    tags = models.CharField(max_length=30, default='-')
    catname = models.CharField(max_length=30, default='-')
    views = models.IntegerField(default=0)
    catid = models.IntegerField(default=0)
    picname = models.CharField(max_length=20, default='-')
    ocatid = models.IntegerField(default=0)
    confirm = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    def __str__(self):
        return self.name