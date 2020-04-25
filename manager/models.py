from django.db import models

# Create your models here.

class Manager(models.Model):
    
    name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)

    def __str__(self):
        return self.username + ' | ' + str(self.pk)


    