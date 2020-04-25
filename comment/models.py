from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length = 30)
    comment = models.TextField()
    status = models.IntegerField(default=0)
    news_id = models.IntegerField()
    date = models.CharField(max_length = 30)
    time = models.CharField(max_length = 20)

    def __str__(self):
        return self.name + ' | ' + str(self.pk)
