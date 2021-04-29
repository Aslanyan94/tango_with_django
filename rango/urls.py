from django.urls import path
from rango.views import about_page
from rango.views import about, index

urlpatterns = [
    # path("about/", about_page),
    path("", index),
    path("about/", about, name="about")
]
