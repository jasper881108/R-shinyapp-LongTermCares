from django.shortcuts import render

# Create your views here.

def home_screen_view(request,*args,**kwargs):
    context={}
    return render(request,'home_screen_view.html',context)

