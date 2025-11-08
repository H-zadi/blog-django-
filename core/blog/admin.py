from django.contrib import admin
from .models import Category,Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=('auhter','title','status','creat_date','category','update_date')

admin.site.register(Category)
admin.site.register(Post)