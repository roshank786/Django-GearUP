from django.shortcuts import render

from django.views import View

from myapp.forms import BrandForm

# Create your views here.




class CarCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance = BrandForm()

        return render(request,"car_add.html",{"form":form_instance})
