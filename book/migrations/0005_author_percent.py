# Generated by Django 3.2.7 on 2021-10-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20211008_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='percent',
            field=models.PositiveSmallIntegerField(default=20, verbose_name='Percent'),
        ),
    ]