# Generated by Django 3.0.2 on 2020-03-16 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]