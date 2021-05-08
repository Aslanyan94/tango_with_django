from django.urls import path
from rango.views import about_page
from rango.views import about, index, category

urlpatterns = [
    # path("about/", about_page),
    path("", index),
    path("about/", about, name="about"),
    path("category/", category, name="category")
]
