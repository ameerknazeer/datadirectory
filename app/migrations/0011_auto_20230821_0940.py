# Generated by Django 3.2.20 on 2023-08-21 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_student_add_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='session_year',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
