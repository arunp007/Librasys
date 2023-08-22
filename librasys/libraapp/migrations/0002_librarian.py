# Generated by Django 4.0.1 on 2023-08-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField(max_length=50)),
                ('lastname', models.TextField(max_length=50)),
                ('library_name', models.TextField(max_length=50)),
                ('library_location', models.TextField(max_length=50)),
                ('email', models.TextField(max_length=50)),
                ('phone', models.TextField(max_length=50)),
                ('password', models.TextField(max_length=50)),
                ('cpassword', models.TextField(max_length=50)),
            ],
        ),
    ]