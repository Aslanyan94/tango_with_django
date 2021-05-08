from django.contrib.auth.models import User
from django.db import models

# class User(models.Model):
#     user ...


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to=)
    created_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_time}: {self.user.username}"


class Category(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


class ImageModel(models.Model):
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name_plural = "Images"