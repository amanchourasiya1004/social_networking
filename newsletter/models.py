from django.db import models

# Create your models here.

class Newsletter(models.Model):
    
    contact = models.CharField(max_length = 30)
    status = models.CharField(max_length = 30)

    def __str__(self):
        return self.contact + ' | ' + str(self.pk)
