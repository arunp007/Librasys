# Generated by Django 4.0.1 on 2023-09-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraapp', '0009_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('message', models.TextField(max_length=100)),
            ],
        ),
    ]
