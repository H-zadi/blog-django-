from django.db import models
from accunts.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    ''''
    thes class  for post app
    '''
    auhter=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=250)
    content=models.TextField()
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    creat_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name