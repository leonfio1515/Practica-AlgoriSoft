# Generated by Django 4.0.5 on 2022-09-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='category',
            field=models.ManyToManyField(to='MiApp.category'),
        ),
    ]
