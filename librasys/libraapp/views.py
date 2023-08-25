from django.shortcuts import render, redirect
from django.http import HttpResponse
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
    

    

