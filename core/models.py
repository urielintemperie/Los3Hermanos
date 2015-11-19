from django.db import models

# Create your models here.

class Rubro(models.Model):
    nombre=models.CharField(max_length=64)
    def __unicode__(self):
        return self.nombre


class Producto (models.Model):

    precio=models.IntegerField()
    nombre=models.CharField(max_length=64)
    rubro=models.ForeignKey(Rubro)
    def __unicode__ (self):
        return self.nombre

class Pedido (models.Model):

    producto=models.ForeignKey(Producto)
    fecha=models.DateField()
    cantidad=models.IntegerField()
    costoUnidad=models.IntegerField()
    def __unicode__ (self):
        return str(self.fecha) + " | " + self.producto.nombre + " | " + str(self.cantidad) + " | " + str(self.pk)

class Reserva (models.Model):

    producto=models.ForeignKey(Producto)
    fecha=models.DateField()
    cantidad=models.IntegerField()
    costoUnidad=models.IntegerField()
    def __unicode__ (self):
        return str(self.fecha) + " | " + self.producto.nombre + " | " + str(self.cantidad) + " | " + str(self.pk)

