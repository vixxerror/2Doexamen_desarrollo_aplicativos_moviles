
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    imagen = models.ImageField(upload_to='categorias',blank=True,null=True)

    def __str__(self):
        return self.nombre

class Product(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos',blank=True,null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre