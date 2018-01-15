from django.db import models

# Create your models here.
class UserMain(models.Model):
    UserName = models.CharField(max_length=140)
    Password = models.CharField(max_length=140)
    Type = models.CharField(max_length=140) 
    College = models.CharField(max_length=140,default="ipec")
    Email = models.EmailField()
    Pno = models.IntegerField()
    def __str__(self):
        return self.UserName

