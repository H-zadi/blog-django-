from django.shortcuts import render

# Create your views here.
def indexviews(request):
    return render(request,'index.html')