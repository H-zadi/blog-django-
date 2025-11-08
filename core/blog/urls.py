
from django.urls import path
from.views import indexviews
from django.views.generic import TemplateView


urlpatterns = [
    path('fbv',indexviews,name='test'),
    path("cbv", TemplateView.as_view(template_name="index.html")),
]