from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Taller) #CAPAZ TIENE QUE SER ANY
admin.site.register(Compras)
admin.site.register(RRHH)
admin.site.register(Inventario)
