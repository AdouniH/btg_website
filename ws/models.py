from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=9000)

    def __str__(self):
        return self.name