from django import forms
from .models import Category

# class CategoryForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     surename = forms.CharField(max_length=10)


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=30)

    class Meta:
        model = Category
        fields = ("name", )
