from django.shortcuts import render
from django.http import HttpResponse

def user_home(request):
    return render(request, 'user_home.html')

def user_login(request):
    return render(request, 'user_login.html')

def user_signup(request):
    return render(request, 'user_signup.html')

def librarian_home(request):
    return render(request, 'librarian_home.html')

def librarian_login(request):
    return render(request, 'librarian_login.html')

def librarian_signup(request):
    return render(request, 'librarian_signup.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def admin_signup(request):
    return render(request, 'admin_signup.html')
