# Generated by Django 3.2.20 on 2023-08-18 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(4, 'HoD'), (5, 'STAFF'), (6, 'STUDENT')], default=1, max_length=50),
        ),
    ]