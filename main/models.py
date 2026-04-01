from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    npm = models.CharField(max_length=20)
    description = models.TextField()
    photo = models.ImageField(upload_to='members/')

    def __str__(self):
        return self.name