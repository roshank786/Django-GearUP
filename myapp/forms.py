from django import forms

from myapp.models import Car,Brand




class BrandForm(forms.ModelForm):

    fields = ["name","country"]