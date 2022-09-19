# Generated by Django 4.0.5 on 2022-07-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_cursos_dictados_horas'),
    ]

    operations = [
        migrations.CreateModel(
            name='workshops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop', models.CharField(max_length=200, verbose_name='Nombre')),
                ('horas', models.PositiveIntegerField(verbose_name='Horas')),
                ('congreso', models.CharField(max_length=200, verbose_name='Congreso')),
                ('anio', models.DateTimeField(max_length=4, verbose_name='Año')),
            ],
        ),
    ]
