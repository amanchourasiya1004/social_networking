from django.db import models

# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length=20)
    about = models.TextField()
    fb = models.CharField(max_length=20, default='-')
    yt = models.CharField(max_length=20, default='-')
    tw = models.CharField(max_length=20, default='-')
    tell = models.CharField(max_length=12, default='-')
    link = models.CharField(max_length=20, default='-')
    set_name = models.CharField(max_length=20, default='-')
    picurl = models.CharField(max_length = 50, default='-')
    picurl2 = models.CharField(max_length=50, default='-')
    picname = models.CharField(max_length = 50, default='-')
    picname2 = models.CharField(max_length = 50, default='-')

    def __str__(self):
        return self.set_name + ' | ' + str(self.pk)