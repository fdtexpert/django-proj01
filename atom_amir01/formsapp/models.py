from django.db import models
# Create your models here.

class SystemUsers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return (self.first_name + " " + self.last_name)
