from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' ' + self.description
    

class CustomUser(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.user_name