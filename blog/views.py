from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView

from .models import Bot,Model,Product,Client1,Client2,Fermer,Late,We,Name,Our,Lorem,Post
from .forms import ContactForms,NewForms
# Create your views here.


def index(request):
    bots = Bot.objects.all()
    models = Model.objects.all()
    products = Product.objects.all()
    clients1 = Client1.objects.all()
    clients2 = Client2.objects.all()
    fermers = Fermer.objects.all()
    lates  = Late.objects.all()

    news = NewForms(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "bots":bots,
        "models":models,
        "products":products,
        "clients1":clients1,
        "clients2":clients2,
        "fermers":fermers,
        "lates":lates,
        "news":news
    }
    return render(request,"index.html",context=context)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'price','slug','img')
    template_name = 'coursesEdit.html'



class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'productsDelete.html'
    success = reverse_lazy('index')

class ProductCreateView(CreateView):
    model = Product
    template_name = "productsCreate.html"
    fields = ("name","price", "img","slug" )

def productsDetail(request, products):
    products = get_object_or_404(Product,slug=products)
    context ={
        "products":products
    }
    return render(request,"productsDetail.html",context=context)



def about(request):
    wes = We.objects.all()
    news = NewForms(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "wes":wes,
        "news":news
    }
    return render(request,"about.html",context=context)

def blog(request):
    lorems = Lorem.objects.all()
    posts = Post.objects.all()
    news = NewForms(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "lorems":lorems,
        "posts":posts,
        "news":news
    }
    return render(request,"blog.html",context=context)

def contact(request):
    contact = ContactForms(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    news = NewForms(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "contact":contact,
        "news":news
    }
    return render(request,"contact.html",context=context)

def detail(request):
    news = NewForms(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "news":news
    }
    return render(request,"detail.html",context=context)

def feature(request):
    news = NewForms(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context =  {
        "news":news
    }
    return render(request,"feature.html",context=context)

def product(request):
    ours = Our.objects.all()
    news = NewForms(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "ours":ours,
        "news":news
    }
    return render(request,"product.html",context=context)

def service(request):
    names = Name.objects.all()
    news = NewForms(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "names":names,
        "news":news
    }
    return render(request,"service.html",context=context)

def team(request):
    news = NewForms(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "news":news
    }
    return render(request,"team.html",context=context)

def testimonial(request):
    news = NewForms(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "news":news
    }
    return render(request,"testimonial.html",context=context)


def modelsdetailview(request,id):
    try:
        models=Model.objects.get(id=id)
        context = {
            "models":models
        }
    except models.DoesNotExist:
        raise Http404("No models found")
    return render(request,"models_detail.html",context=context)

def productsdetailview(request,id):
    try:
        products=Product.objects.get(id=id)
        context = {
            "products":products
        }
    except products.DoesNotExist:
        raise Http404("No products found")
    return render(request,"products_Detail.html",context=context)


def fermersdetailview(request,id):
    try:
        fermers=Fermer.objects.get(id=id)
        context = {
            "fermers":fermers
        }
    except fermers.DoesNotExist:
        raise Http404("No fermers found")
    return render(request,"fermers_Detail.html",context=context)

def latesdetailview(request,id):
    try:
        lates=Late.objects.get(id=id)
        context = {
            "lates":lates
        }
    except lates.DoesNotExist:
        raise Http404("No lates found")
    return render(request,"lates_Detail.html",context=context)


def wesdetailview(request,id):
    try:
        wes=We.objects.get(id=id)
        context = {
            "wes":wes
        }
    except wes.DoesNotExist:
        raise Http404("No wes found")
    return render(request,"wes_Detail.html",context=context)

def namesdetailview(request,id):
    try:
        names=Name.objects.get(id=id)
        context = {
            "names":names
        }
    except names.DoesNotExist:
        raise Http404("No names found")
    return render(request,"names_Detail.html",context=context)

def oursdetailview(request,id):
    try:
        ours=Our.objects.get(id=id)
        context = {
            "ours":ours
        }
    except ours.DoesNotExist:
        raise Http404("No ours found")
    return render(request,"ours_Detail.html",context=context)

def postsdetailview(request,id):
    try:
        posts=Post.objects.get(id=id)
        context = {
            "posts":posts
        }
    except posts.DoesNotExist:
        raise Http404("No posts found")
    return render(request,"posts_Detail.html",context=context)


def loremsdetailview(request,id):
    try:
        lorems=Lorem.objects.get(id=id)
        context = {
            "lorems":lorems
        }
    except lorems.DoesNotExist:
        raise Http404("No lorems found")
    return render(request,"lorems_Detail.html",context=context)























































































































































































































































