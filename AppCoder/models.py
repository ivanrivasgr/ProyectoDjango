from django.db import models

# Create your models here.


class Taller (models.Model):
    vehiculo=models.CharField(max_length=40)
    modelo=models.CharField(max_length=40)
    ano=models.IntegerField()
    status=models.CharField(max_length=40)
    trabajosactivos=models.CharField(max_length=500)
    trabajosporhacer=models.CharField(max_length=500)

    #def calcular_anosoperativos(self):
        #hoy = datetime.date.today()
        #anosoperativos = hoy.year - self.ano.year
        #if hoy < datetime.date(hoy.year, self.ano.month, self.ano.day):
        #    anosoperativos -= 1
        
        #return anosoperativos
    

class Compras (models.Model):
    Repuesto=models.CharField(max_length=40)
    tipoderepuesto=models.CharField(max_length=40)
    modeloderepuesto=models.CharField(max_length=40)
    tipodevehiculo=models.CharField(max_length=40)
    fecha=models.DateField()
    precio=models.IntegerField()
    comprador=models.CharField(max_length=40)
    proveedor=models.CharField(max_length=40)

class RRHH (models.Model):
    nombre=models.CharField(max_length=40)
    cargo=models.CharField(max_length=40)
    fechadenac=models.DateField()
    anodeingreso=models.DateField()
    supervisordirecto=models.CharField(max_length=40)
    sueldo=models.IntegerField()

    #def calcular_anosenlaempresa(self):
    #    hoy = datetime.date.today()
    #    anosenlaempresa = hoy.year - self.ano.year
    #    if hoy < datetime.date(hoy.year, self.ano.month, self.ano.day):
    #        anosenlaempresa -= 1
        
    #    return anosenlaempresa
    

class Inventario (models.Model):
    item=models.CharField(max_length=40)
    tipodeitem=models.CharField(max_length=40)
    modelodeitem=models.CharField(max_length=40)
    tipodevehiculo=models.CharField(max_length=40)
    ano=models.IntegerField()
    fechadecompra=models.DateField()
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    ultimoproveedor=models.CharField(max_length=40)
    ultimocomprador=models.CharField(max_length=40)

    #def calcular_ultimacompra(self):
        #hoy = datetime.date.today()
        #ultimacompra = hoy.year - self.ano.year
        #if hoy < datetime.date(hoy.year, self.ano.month, self.ano.day):
        #    ultimacompra -= 1
        
        #return ultimacompra

    #def calcular_ultimoprecio(self):
        #hoy = datetime.date.today()
        #ultimoprecio = hoy.year - self.ano.year
        #if hoy < datetime.date(hoy.year, self.ano.month, self.ano.day):
        #    ultimoprecio -= 1
        
        #return ultimoprecio