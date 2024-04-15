from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Composts, Orders
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists.')
            return redirect('signup')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'User created successfully.')
        return redirect('login')
    return render(request, 'signup_page.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. User does not exist.')
            return redirect('signup')
    return render(request, 'login_page.html')

def home_view(request):
    return render(request, 'home_page.html')

def services_view(request):
    composts = Composts.objects.all()
    if request.method == "POST":
        compost_id = request.POST.get('compost_id', False)
        quantity = request.POST.get('quantity', False)

        try:
            compost = Composts.objects.get(pk=compost_id)
            total_cost = compost.cost_per_unit * int(quantity)
            order = Orders(compost_id=compost_id, quantity=quantity, total_cost=total_cost, date_of_purchase='2023-09-16')
            order.save()
            return redirect('home')
        except ObjectDoesNotExist:
            return HttpResponse("Invalid Compost ID")
    return render(request, 'services_page.html', {'composts': composts})


def about_view(request):
    return render(request, 'about_page.html')

def analysis_view(request):
    return render(request, 'analysis_page.html')

'''def add_order(request):
    print("request method called: ", request.method)
    if request.method == "POST":
        compost_id = request.POST.get('compost_id', False)
        quantity = request.POST.get('quantity', False)

        try:
            compost = Composts.objects.get(pk=compost_id)
            total_cost = compost.cost_per_unit * int(quantity)
            order = Orders(compost_id=compost, quantity=quantity, total_cost=total_cost, date_of_purchase='2023-09-16')
            order.save()
            return redirect('home')
        except ObjectDoesNotExist:
            return HttpResponse("Invalid Compost ID")

    return render(request, 'services_page.html')'''

'''if request.method == "POST":
        name = request.POST.get('username', False)
        passw = request.POST.get('password', False)
        em = request.POST.get('email', False)
        num = request.POST.get('phone', False)
        record = CustomUser(Name = name, Phoneno = num, Email = em, Passwd = passw)
        record.save()
    return render(request, "signup.html")'''