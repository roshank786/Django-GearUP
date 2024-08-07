from django import forms

from myapp.models import Car,Brand




class BrandForm(forms.ModelForm):

    class Meta:
        
        model = Brand

        fields = ["name","country"]

        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "country":forms.TextInput(attrs={"class":"form-control"}),
        }