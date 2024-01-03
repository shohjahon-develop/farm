from django.db import models
from django.urls import reverse


# Create your models here.

class Bot(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')


    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    slug = models.SlugField(max_length=300)
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("productsDetail", args=[self.slug])


class Client1(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Client2(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Fermer(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='index/img')
    bio = models.TextField()

    def __str__(self):
        return self.name



    def __str__(self):
        return self.name

class We(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='about/img')
    bio = models.TextField()

    def __str__(self):
        return self.name


class Name(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    img =models.ImageField(upload_to='service/img')

    def __str__(self):
        return self.name


class Our(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    img = models.ImageField(upload_to='product/img')

    def __str__(self):
        return self.name


class Lorem(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='blog/img')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=300)
    subject = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='blog/img')

    def __str__(self):
        return self.name


class Late(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    slug = models.SlugField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='index/img')



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("latesdetail", args=[self.slug])




class New(models.Model):
    email  = models.EmailField(max_length=300)

    def __str__(self):
        return self.email
















































































































































































