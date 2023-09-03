from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import random
from django.core.files.storage import FileSystemStorage
from.models import *

def user_home(request):
    return render(request, 'user_home.html')

def user_login(request):
    email = None
    password = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

    try:
        current_user = User.objects.get(email = email, password = password)
        request.session['xyz'] = current_user.id
        return redirect('user_home')
    
    except User.DoesNotExist:
        return render(request, 'user_login.html', {'message': 'You entered a wrong email id and password'})

def user_logout(request):
    request.session.flush()
    return redirect('user_login')

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

def user_table(request):
    user_data = User.objects.all()
    return render(request, 'user_table.html', { 'user': user_data })

def user_delete(request,id):
    User.objects.get(id = id).delete()
    return redirect('user_table')

def user_update(request,id):
    update_data = ""
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
        User.objects.filter(id = id).update(firstname = fname, lastname = lname, day = day, month = month, year = year, gender = gender, address = address, location = location, username = username, email = email, password = password, cpassword = cpassword)
        return redirect('user_table')
    
    else:
        update_data = User.objects.get(id = id)
        return render(request, 'user_signup.html', { 'update': update_data })

def librarian_home(request):
    return render(request, 'librarian_home.html')

def librarian_login(request):
    email = None
    password = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

    try:
        current_librarian = Librarian.objects.get(email = email, password = password)
        request.session['xyz'] = current_librarian.id
        return redirect('librarian_home')
    
    except Librarian.DoesNotExist:
        return render(request, 'librarian_login.html', {'message': "You entered a wrong email id and password"})

def librarian_logout(request):
    request.session.flush()
    return redirect('librarian_login')

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

def librarian_table(request):
    librarian_data = Librarian.objects.all()
    return render(request, 'librarian_table.html', { 'librarian': librarian_data })

def librarian_delete(request,id):
    Librarian.objects.get(id = id).delete()
    return redirect('librarian_table')

def librarian_update(request,id):
    update_data = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        library_name = request.POST['library_name']
        library_location = request.POST['library_location']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        Librarian.objects.filter(id = id).update(firstname = fname, lastname = lname, library_name = library_name, library_location = library_location, email = email, phone = phone, password = password, cpassword = cpassword)
        return redirect('librarian_table')
    
    else:
        update_data = Librarian.objects.get(id = id)
        return render(request, 'librarian_signup.html', { 'update': update_data })


def admin_home(request):
    return render(request, 'admin_home.html')

def admin_login(request):
    email = None
    password = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

    try:
        current_admin = Admin.objects.get(email = email, password = password)
        request.session['xyz'] = current_admin.id
        return redirect('admin_home')
    except Admin.DoesNotExist:

        return render(request, 'admin_login.html',{'message': "You entered a wrong email id and password"})

def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')

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

def admin_table(request):
    admin_data = Admin.objects.all()
    return render(request, 'admin_table.html', { 'admin': admin_data })

def admin_delete(request,id):
    Admin.objects.get(id = id).delete()
    return redirect('admin_table')

def admin_update(request,id):
    update_data = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        Admin.objects.filter(id = id).update(firstname = fname, lastname = lname, email = email, phone = phone, password = password, cpassword = cpassword)
        return redirect('admin_table')

    else:
        update_data = Admin.objects.get(id = id)
        return render(request, 'admin_signup.html', { 'update': update_data })
    

def add_books(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        author = request.POST['author']
        price = request.POST['price']
        image = request.FILES['image']
        file_name = str(random())+image.name
        image.name = file_name
        file_object = FileSystemStorage()
        file_object.save(file_name, image)
        object_details = Books_data(name = name, description = description, author = author, price = price, image = image)
        object_details.save()

    else:
        image = False
    return render(request, 'add_books.html')


def user_books(request):
    books_data = Books_data.objects.all()
    return render(request, 'user_books.html', {'books': books_data})


def librarian_books(request):
    books_data = Books_data.objects.all()
    return render(request, 'librarian_book.html', {'books': books_data})

def book_table(request):
    book_details = Books_data.objects.all()
    return render(request, 'book_table.html', {'book': book_details})

def book_delete(request, id):
    Books_data.objects.get(id = id).delete()
    return redirect('book_table')

def book_update(request, id):
    update_data = ""
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']
        file_name = str(random())+image.name
        image.name = file_name
        file_object = FileSystemStorage()
        file_object.save(file_name,image)
        Books_data.objects.filter(id = id).update(name = name, author = author, description = description, price = price, image = image)
        return redirect('book_table')
    
    else:
        update_data = Books_data.objects.get(id = id)
        return render(request, 'add_books.html', {'update': update_data})


def buyer(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        location = request.POST['location']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        book = request.POST['book']
        author = request.POST['author']
        purchase_date = request.POST['purchase_date']
        return_date = request.POST['return_date']
        return_policy = request.POST['return_policy']
        buyer_details = Buyer(fullname = fullname, location = location, address = address, email = email, phone = phone, book = book, author = author, purchase_date = purchase_date, return_date = return_date, return_policy = return_policy)
        buyer_details.save()
        return redirect('order')
    return render(request, 'buyer.html')

def order(request):
    return render(request, 'order.html')

def buyer_table(request):
    buyer_details = Buyer.objects.all()
    return render(request, 'buyer_table.html', {'buyer': buyer_details})

def buyer_delete(request,id):
    Buyer.objects.get(id = id).delete()
    return redirect('buyer_table')

def buyer_update(request,id):
    update_data = ""
    if request.method == 'POST':
        fullname = request.POST['fullname']
        location = request.POST['location']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        book = request.POST['book']
        author = request.POST['author']
        purchase_date = request.POST['purchase_date']
        return_date = request.POST['return_date']
        return_policy = request.POST['return_policy']
        Buyer.objects.filter(id = id).update(fullname = fullname, location = location, address = address, email = email, phone = phone, book = book, author = author, purchase_date = purchase_date, return_date = return_date, return_policy = return_policy)
        return redirect('buyer_table')

    else:
        update_data = Buyer.objects.get(id = id)
        return render(request, 'buyer.html', {'update' : update_data})






