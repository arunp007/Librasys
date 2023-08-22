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




