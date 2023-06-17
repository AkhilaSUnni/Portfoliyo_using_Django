from django.db import models

# Create your models here.
class pictures(models.Model):
    image =models.ImageField(upload_to='mypics/')
 

class formdata(models.Model):
  
    uname = models.CharField(max_length=10)
    em = models.EmailField()
    phone = models .IntegerField()
    message = models.CharField(max_length=100)
   
    def __str__(self):
       return self.uname