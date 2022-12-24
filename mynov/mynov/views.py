from django.shortcuts import render, redirect #untuk memanggil file html
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse #format html langsung ditulis didalam HttpRespon
from django.contrib.auth import logout

from mywisata.models import *
#import requests

def index(request):
    template_name = 'front/index.html'
    artikel = Artikel.objects.all()
    context = {
        'title':'halaman awal',
        'artikel' :artikel,
    }
    return render(request, template_name, context)

def about(request):
    template_name = "front/about.html"
    context = {
        'title' : 'about me',
        'welcome' : 'ini page about',
    }
    return render(request, template_name, context)

def blog(request):
    template_name = "front/blog.html"
    artikel = Artikel.objects.all()
    context = {
        'title' : 'my blog',
        'artikel' :blog,
    }
    return render(request, template_name, context)

def gallery(request):
    template_name = "front/gallery.html"
    artikel = Artikel.objects.all()
    context = {
        'title' : 'my gallery',
        'artikel' :gallery,
    }
    return render(request, template_name, context)

def deskripsi(request):
    template_name = "front/deskripsi.html"
    artikel = Artikel.objects.all()
    context = {
        'title' : 'my service',
        'artikel' :deskripsi,
    }
    return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
        print('sudah login')
        redirect('tabel_artikel')

    template_name = "front/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #data ada
            print('username benar')
            auth_login(request, user)
            return redirect('index')
        else:
            #data tidak ada
            print('username salah')

    context = {
        'title' : 'from login',
        #'artikel' :login,
    }
    return render(request, template_name, context)

def logout_views(request):
    logout(request)
    return redirect('index')

def artikel_detail(request, id):
    template_name = "front/artikel_detail.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'artikel detail',
        'artikel' :artikel,
    }
    return render(request, template_name, context)