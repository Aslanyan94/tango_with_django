from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def about_page(request):
    return HttpResponse("<h1>Rango about page</h1>")


def about(request):
    return HttpResponse("Rango says hey there partner!")


def index(request):
    contex_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, template_name="rango/index.html", context=contex_dict)