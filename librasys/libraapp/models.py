from django.db import models

class User(models.Model):
    firstname = models.TextField(max_length=50)
    lastname = models.TextField(max_length=50)
    day = models.TextField(max_length=50)
    month = models.TextField(max_length=50)
    year = models.TextField(max_length=50)
    gender = models.TextField(max_length=50)
    address = models.TextField(max_length=50)
    location = models.TextField(max_length=50)
    username = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    phone = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
    cpassword = models.TextField(max_length=50)

class Meta:
    db_table = 'user_registration'


class Librarian(models.Model):
    firstname = models.TextField(max_length=50)
    lastname = models.TextField(max_length=50)
    library_name = models.TextField(max_length=50)
    library_location = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    phone = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
    cpassword = models.TextField(max_length=50)

class Meta:
    db_table = 'librarian_registration'


    
class Admin(models.Model):
    firstname = models.TextField(max_length=50)
    lastname = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    phone = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
    cpassword = models.TextField(max_length=50)

class Meta:
    db_table = 'admin_registration'


class Books_data(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=100)
    author = models.TextField(max_length=50)
    price = models.TextField(max_length=50)
    image = models.CharField(max_length=200)

class Meta:
    db_table = 'books'


class Buyer(models.Model):
    fullname = models.TextField(max_length=100)
    location = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    book = models.TextField(max_length=100)
    author = models.TextField(max_length=100)
    purchase_date = models.TextField(max_length=100)
    return_date = models.TextField(max_length=100)
    return_policy = models.TextField(max_length=100)

class Meta:
    db_table = 'buyer_details'




