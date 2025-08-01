from django.db import models

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True, primary_key=True)
    password = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.email
    