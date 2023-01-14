from django import forms
 
class TallerForm(forms.Form):
    vehiculo = forms.CharField() 
    modelo = forms.CharField()
    ano = forms.IntegerField() #(label="Año del vehiculo", widget=SelectDateWidget(years=range(1900, 2024)) )
    trabajosactivos = forms.CharField() 
    trabajosporhacer = forms.CharField()
    status = forms.ChoiceField(
        #widget=forms.Select,
        choices=[
        ('Operativo', 'Operativo'),
        ('Inoperativo', 'Inoperativo'),
        ('Desincorporado', 'Desincorporado'),
        ])

    
class ComprasForm(forms.Form):
    Repuesto=forms.CharField()
    tipoderepuesto=forms.CharField()
    modeloderepuesto=forms.CharField()
    tipodevehiculo=forms.CharField()
    fecha=forms.DateField()
    precio=forms.IntegerField()
    comprador=forms.CharField()
    proveedor=forms.CharField()

class RRHHForm(forms.Form):
    nombre=forms.CharField()
    cargo=forms.ChoiceField(
        #widget=forms.Select,
        choices=[
        ('Gerente', 'Gerente'),
        ('Coordinador de Flota', 'Coordinador de Flota'),
        ('Jefe de Taller', 'Jefe de Taller'),
        ('Analista Administrativo', 'Analista Administrativo'),
        ('Analista de Compras', 'Analista de Compras'),
        ('Analista Contable', 'Analista Contable'),
        ('Analista de RRHH', 'Analista de RRHH'),
        ('Mecanico', 'Mecanico'),
        ('Ayudante de Mecanico', 'Ayudante de Mecanico'),
        ('Chofer carga pesada', 'Chofer carga pesada'),
        ('Chofer carga liviana', 'Chofer carga liviana'),
        ('Seguridad', 'Seguridad'),
        ('Almacenista', 'Almacenista'),
        ('Cocinero', 'Cocinero'),
        ])
    fechadenac=forms.DateField() #(label="Fecha de nacimiento", widget=SelectDateWidget(years=range(1934, 2024)) )
    anodeingreso=forms.DateField() #(label="Fecha de ingreso", widget=SelectDateWidget(years=range(2015, 2024)) )
    supervisordirecto=forms.CharField()
    sueldo=forms.IntegerField()

class InventarioForm(forms.Form):
    item=forms.CharField()
    tipodeitem=forms.CharField()
    modelodeitem=forms.CharField()
    tipodevehiculo=forms.CharField()
    ano=forms.IntegerField()
    fechadecompra=forms.DateField() #(label="Fecha de compra", widget=SelectDateWidget(years=range(2015, 2024)) )
    precio=forms.IntegerField()
    cantidad=forms.IntegerField()
    ultimoproveedor=forms.CharField()
    ultimocomprador=forms.CharField()



