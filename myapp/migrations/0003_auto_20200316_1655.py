# Generated by Django 3.0.2 on 2020-03-16 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200227_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='create_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='purchase_date',
        ),
    ]
