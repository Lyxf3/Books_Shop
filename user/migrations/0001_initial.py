# Generated by Django 3.2.7 on 2021-10-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='Email')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is_staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is_active')),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Balance')),
                ('favourite_books', models.ManyToManyField(related_name='Users', to='book.Book', verbose_name='Favourite_books')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
