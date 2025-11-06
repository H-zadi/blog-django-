from django.db import models
from django.contrib.auth.models import(BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import(BaseUserManager,AbstractBaseUser,PermissionsMixin)
# from django.utils.translation import ugettext_lazy as _

# # Create your models here.
# class Post(models.Model):
#     ''''
#     thes class  for post app
#     '''
#     auhter=models.ForeignKey('User',on_delete=models.CASCADE)
#     image=models.ImageField(null=True,blank=True)
#     title=models.CharField(max_length=250)
#     content=models.TextField()
#     status=models.BooleanField()
#     category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
#     creat_date=models.DateTimeField(auto_now_add=True)
#     update_date=models.DateTimeField(auto_now=True)
#     pubilsh_date=models.DateTimeField()

#     def __str__(self):
#         return self.title


# class Category(models.Model):
#     name=models.CharField(max_length=25)

#     def __str__(self):
#         return self.name

class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
          raise ValueError (('the email must be set'))
        email= self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True :
            raise ValueError (_('is not true s staff'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('is not superuser true'))
        return self.create_user(email,password,**extra_fields)
        




class User(AbstractBaseUser,PermissionsMixin):

    '''
    custum user app

    '''
    
    email= models.EmailField(max_length=255,unique=True)
    is_superuser =models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    # is_verfied=models.BooleanField(default=False)
    firest_name=models.CharField(max_length=200)

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=[]

    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    objects=UserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firs_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=100)

    image=models.ImageField(blank=True,null=True)
    desc=models.TextField(max_length=500)
    creat_data=models.DateTimeField(auto_now_add=True)
    update_data=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

@receiver(post_save,sender=User)

def save_profile(sender,instance,created,**kwoargs):
    if created:

     Profile.objects.create(user=instance)