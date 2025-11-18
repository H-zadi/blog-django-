
from django.urls import path

from django.views.generic import TemplateView
from .import views

app_name='blog'

urlpatterns = [
    path('post/',views.postlist.as_view(),name='list'),
    path('create/',views.createpost.as_view(),name='create'),
    path('detail/<int:pk>',views.detail_post.as_view(),name='detail1'),
    path('delet/<int:pk>',views.deletpost.as_view(),name='delet1')

]