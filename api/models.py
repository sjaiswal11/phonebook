from django.db import models

# Create your models here.

class ContactsModel(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.IntegerField()
    user = models.CharField(max_length = 100, null=True, blank="True")
    
    def __str__(self):
        return self.name
    