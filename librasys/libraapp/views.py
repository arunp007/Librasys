from django.shortcuts import render
from django.http import HttpResponse
from.models import *

def user_home(request):
    return render(request, 'user_home.html')

def user_login(request):
    return render(request, 'user_login.html')

def user_signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']
        gender = request.POST['gender']
        address = request.POST['address']
        location = request.POST['location']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user_details = User(firstname = fname, lastname = lname, day = day, month = month, year = year, gender = gender, address = address, location = location, username = username, email = email, phone = phone, password = password, cpassword = cpassword)
        user_details.save()
    return render(request, 'user_signup.html')

def librarian_home(request):
    return render(request, 'librarian_home.html')

def librarian_login(request):
    return render(request, 'librarian_login.html')

def librarian_signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        library_name = request.POST['library_name']
        library_location = request.POST['library_location']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        librarian_details = Librarian(firstname = fname, lastname = lname, library_name = library_name, library_location = library_location, email = email, phone = phone, password = password, cpassword = cpassword)
        librarian_details.save()
    return render(request, 'librarian_signup.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def admin_signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        admin_details = Admin(firstname = fname, lastname = lname, email = email, phone = phone, password = password, cpassword = cpassword)
        admin_details.save()
    return render(request, 'admin_signup.html')
