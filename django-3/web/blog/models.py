from django.db import models
from datetime import datetime

class Employee(models.Model):
    names = models.CharField(max_length=150, verbose_name="Nombres")
    dni = models.CharField(max_length=10, unique=True, verbose_name="DNI")
    date_joined = models.DateField(default=datetime.now, verbose_name="Fecha de registro")
    date_creation = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now_add=True)    
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    cvitae = models.FileField(upload_to="cvitae/%Y/%m/%d", null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name= "Empleado"
        verbose_name_plural = "Empleados"
        db_table = "empleado"
        ordering = ["id"]