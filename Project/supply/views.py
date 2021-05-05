from django.shortcuts import render

# Create your views here.
def supply_view(request,*args,**kwargs):
    context={}
    return render(request,'supply.html',context)