from django.shortcuts import render

# Create your views here.
def demand_view(request,*args,**kwargs):
    context={}
    return render(request,'demand.html',context)