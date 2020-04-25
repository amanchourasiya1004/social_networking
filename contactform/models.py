from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.TextField()
    email = models.CharField(max_length = 50)
    msg = models.TextField()
    date = models.CharField(max_length = 10,  default='-')
    def __str__(self):
        return self.name + ' | ' + str(self.pk)