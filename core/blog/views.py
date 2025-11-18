from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView, CreateView

from .models import Post
from .forms import Postform
# Create your views here.


class postlist(ListView):
    model=Post
    template_name='blog/index.html/'
    context_object_name='postlist'


class createpost(CreateView):
    model=Post
    fields=['image','title','category','auhter']
    success_url='/post/'

    def form_valid(self, form):
        form.instance.auhder=self.request.user
        return super().form_valid(form)



class detail_post(DetailView):
    model=Post


class deletpost(DeleteView):
    model=Post
    context_object_name='del'

    success_url='/post/'
