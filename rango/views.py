from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Page, Category
from rango.forms import CategoryForm

# Create your views here.


def about_page(request):
    return HttpResponse("<h1>Rango about page</h1>")


def about(request):
    return HttpResponse("Rango says hey there partner!")


def index(request):
    contex_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, template_name="rango/index.html", context=contex_dict)

# category save via forms.Form
# def category(request):
#     form = CategoryForm()
#     if request.method == "POST":
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             cat = Category()
#             cat.name = form.cleaned_data["name"]
#             cat.save(commit=False)
#             user = request.user
#             cat.user = user
#             cat.save(commit=True)
#             print(form.cleaned_data)
#             return render(request, "rango/category.html", context={"valid": "is valid"})
#         return render(request, "rango/category.html", context={"valid": "is not valid"})
#     return render(request, "rango/category.html", context={"form": form})

# save category via forms.ModelForm
def category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return render(request, "rango/category.html", context={"valid": "is valid"})
        return render(request, "rango/category.html", context={"valid": "is not valid"})
    return render(request, "rango/category.html", context={"form": form})