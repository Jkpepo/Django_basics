from django.db import models

# Create your models here.


class Vehiculo(models.Model):
    nombres=models.CharField(max_length=50,null=False,blank=False)
    tipo=models.CharField(max_length=50,null=False,blank=False)
    foto=models.ImageField(upload_to='fotos/')
    fecha=models.DateTimeField(null=False,blank=False)
    telefono=models.CharField(max_length=10)
   
    def __str__(self):
        return  f"{self.nombres}"