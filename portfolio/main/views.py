from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from.models import *
# Create your views here.
def index(request):
    d={
        'img_field':pictures.objects.all()
    }
    if request.method =='POST':
        name =request.POST.get('user_name')
        email =request.POST.get('user_email')
        phone = request.POST.get('phone')
        msg =request.POST.get('message')
      
        ob = formdata(uname=name,em=email,phone=phone,message=msg)
        ob.save()
        return render(request,'index.html')
    #     print('object saved')
    #     return redirect(about)
    # else:
    #     print('object not saved')
    return render(request,"index.html",d)