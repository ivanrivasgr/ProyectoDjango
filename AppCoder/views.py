from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from AppCoder.static import *
from AppCoder.forms import TallerForm
from AppCoder.forms import ComprasForm
from AppCoder.forms import RRHHForm
from AppCoder.forms import InventarioForm
from AppCoder.models import Taller
from AppCoder.models import Compras
from AppCoder.models import RRHH
from AppCoder.models import Inventario


# Create your views here.


def inicio(request):
      return render(request, 'AppCoder/inicio.html')


def CargaVehiculo(request):

      try:

            if request.method == "POST":
            # Aqui me llega la informacion del html
                  vehiculoFormulario = TallerForm(request.POST)         

                  if vehiculoFormulario.is_valid():
                        informacion = vehiculoFormulario.data
                        vehiculo = Taller(vehiculo=informacion['vehiculo'], modelo=informacion['modelo'], ano=informacion['ano'], status=informacion['status'], trabajosactivos=informacion['trabajosactivos'], trabajosporhacer=informacion['trabajosporhacer'])
                        vehiculo.save()

                        return render(request, "AppCoder/inicio.html")
                  else:
                        vehiculoFormulario = TallerForm()
      
            else:
                  vehiculoFormulario = TallerForm()
      
            return render(request, "AppCoder/CargaVehiculo.html", {"vehiculoFormulario": vehiculoFormulario})

      except:
            return render(request, "AppCoder/Error.html")

def CargaCompra(request):

      try:

            if request.method == "POST":
            # Aqui me llega la informacion del html
                  compraFormulario = ComprasForm(request.POST)

                  if compraFormulario.is_valid():
                        informacion = compraFormulario.data
                        compra = Compras(Repuesto=informacion['Repuesto'], tipoderepuesto=informacion['tipoderepuesto'], fecha=informacion['fecha'], modeloderepuesto=informacion['modeloderepuesto'], comprador=informacion['comprador'], proveedor=informacion['proveedor'], precio=informacion['precio'] )
                        compra.save()

                        return render(request, "AppCoder/inicio.html")
                  else:
                        compraFormulario = ComprasForm()
      
            else:
                  compraFormulario = ComprasForm()
      
            return render(request, "AppCoder/CargaCompra.html", {"compraFormulario": compraFormulario})

      except:
            return render(request, "AppCoder/Error.html")

def CargaEmpleado(request):

      try:

            if request.method == "POST":
            # Aqui me llega la informacion del html
                  empleadoFormulario = RRHHForm(request.POST)         

                  if empleadoFormulario.is_valid():
                        informacion = empleadoFormulario.data
                        empleado = RRHH(nombre=informacion['nombre'], cargo=informacion['cargo'], fechadenac=informacion['fechadenac'], anodeingreso=informacion['anodeingreso'], supervisordirecto=informacion['supervisordirecto'], sueldo=informacion['sueldo'] )
                        empleado.save()

                        return render(request, "AppCoder/inicio.html")
                  else:
                        empleadoFormulario = RRHHForm()
      
            else:
                  empleadoFormulario = RRHHForm()
      
            return render(request, "AppCoder/CargaEmpleado.html", {"empleadoFormulario": empleadoFormulario})

      except:
            return render(request, "AppCoder/Error.html")

def CargaItem(request):

      try:

            if request.method == "POST":
            # Aqui me llega la informacion del html
                  itemFormulario = InventarioForm(request.POST)         

                  if itemFormulario.is_valid():
                        informacion = itemFormulario.data
                        item = Inventario(item=informacion['item'], modelodeitem=informacion['modelodeitem'], ano=informacion['ano'], tipodevehiculo=informacion['tipodevehiculo'], tipodeitem=informacion['tipodeitem'], fechadecompra=informacion['fechadecompra'], precio=informacion['precio'], cantidad=informacion['cantidad'], ultimocomprador=informacion['ultimocomprador'], ultimoproveedor=informacion['ultimoproveedor'])
                        item.save()

                        return render(request, "AppCoder/inicio.html")
                  else:
                        itemFormulario = InventarioForm()
      
            else:
                  itemFormulario = InventarioForm()
      
            return render(request, "AppCoder/CargaItem.html", {"itemFormulario": itemFormulario})

      except:
            return render(request, "AppCoder/Error.html")


def busquedaVehiculo(request):
      return render (request, "AppCoder/busquedaVehiculo.html")

def BuscarVehiculo (request):
      
      if request.GET["vehiculo"]:
            vehiculo = request.GET ['vehiculo']
            vehiculos = Taller.objects.filter(vehiculo__icontains = vehiculo)

            return render (request, "AppCoder/resultadosBusqueda.html", {"vehiculos":vehiculos, "vehiculo": vehiculo})
      
      else:
            return render (request, "AppCoder/busquedaVehiculo.html")



def BusquedaCompras(request):
      return render (request, "AppCoder/BuscarCompra.html")

     
def BuscarCompra(request):
      if request.GET["Repuesto"]:
            Repuesto = request.GET ['Repuesto']
            Repuestos = Compras.objects.filter(Repuesto__icontains = Repuesto)

            return render (request, "AppCoder/ResultadoBusquedaCompras.html", {"Repuestos":Repuestos, "Repuesto": Repuesto})
      
      else:
            return render (request, "AppCoder/BuscarCompra.html")

def busquedaEmpleado(request):
      return render (request, "AppCoder/busquedaEmpleado.html")

def BuscarEmpleado (request):
      
      if request.GET["nombre"]:
            nombre = request.GET ['nombre']
            nombres = RRHH.objects.filter(nombre__icontains = nombre)

            return render (request, "AppCoder/resultadosBusqueda.html", {"nombres":nombres, "nombre": nombre})
      
      else:
            return render (request, "AppCoder/busquedaEmpleado.html")

def busquedaItem(request):
      return render (request, "AppCoder/busquedaItem.html")

def BuscarItem (request):
      
      if request.GET["item"]:
            item = request.GET ['item']
            items = Inventario.objects.filter(item__icontains = item)

            return render (request, "AppCoder/resultadosBusqueda.html", {"items":items, "item": item})
      
      else:
            return render (request, "AppCoder/busquedaItem.html")


##################################################################################################################
##################################################################################################################



                              #           CBV            #


#     VEHICULOS    #

class TallerList(ListView):

      model = Taller
      template_name = 'AppCoder/taller_list.html' ###'AppCoder/jugador_list.html'


class TallerDetalle(DetailView):

      model = Taller
      template_name = 'AppCoder/taller_detalle.html' ###'AppCoder/jugador_detalle.html'

class TallerCreate(CreateView):

      model = Taller
      success_url = '/taller/list'
      fields = ['vehiculo', 'modelo', 'ano', 'status', 'trabajosactivos', 'trabajosporhacer']

class TallerUpdate(UpdateView):

      model = Taller
      success_url = '/taller/list'
      fields = ['vehiculo', 'modelo', 'ano', 'status', 'trabajosactivos', 'trabajosporhacer']

class TallerDelete(DeleteView):

      model = Taller
      success_url = '/taller/list'



#     COMPRAS    #

class ComprasList(ListView):

      model = Compras
      template_name = 'AppCoder/compras_list.html'


class ComprasDetalle(DetailView):

      model = Compras
      template_name = 'AppCoder/compras_detalle.html'

class ComprasCreate(CreateView):

      model = Compras
      success_url = '/compras/list'
      fields = ['Repuesto', 'tipoderepuesto', 'modeloderepuesto', 'tipodevehiculo', 'fecha', 'precio', 'comprador', 'proveedor']

class ComprasUpdate(UpdateView):

      model = Compras
      success_url = '/compras/list'
      fields = ['Repuesto', 'tipoderepuesto', 'modeloderepuesto', 'tipodevehiculo', 'fecha', 'precio', 'comprador', 'proveedor']

class ComprasDelete(DeleteView):

      model = Compras
      success_url = '/compras/list'

#     EMPLEADOS    #

class RRHHList(ListView):

      model = RRHH
      template_name = 'AppCoder/rrhh_list.html'


class RRHHDetalle(DetailView):

      model = RRHH
      template_name = 'AppCoder/rrhh_detalle.html'

class RRHHCreate(CreateView):

      model = RRHH
      success_url = '/rrhh/list'
      fields = ['nombre', 'fechadenac', 'cargo', 'supervisordirecto', 'sueldo', 'anodeingreso']

class RRHHUpdate(UpdateView):

      model = RRHH
      success_url = '/rrhh/list'
      fields = ['nombre', 'fechadenac', 'cargo', 'supervisordirecto', 'sueldo', 'anodeingreso']

class RRHHDelete(DeleteView):

      model = RRHH
      success_url = '/rrhh/list'

#     ITEMS   #

class InventarioList(ListView):

      model = Inventario
      template_name = 'AppCoder/inventario_list.html'


class InventarioDetalle(DetailView):

      model = Inventario
      template_name = 'AppCoder/inventario_detalle.html'

class InventarioCreate(CreateView):

      model = Inventario
      success_url = '/inventario/list'
      fields = ['item', 'tipodeitem', 'modelodeitem', 'tipodevehiculo', 'ano', 'precio', 'fechadecompra', 'cantidad', 'ultimoproveedor', 'ultimocomprador']

class InventarioUpdate(UpdateView):

      model = Inventario
      success_url = '/inventario/list'
      fields = ['item', 'tipodeitem', 'modelodeitem', 'tipodevehiculo', 'ano', 'precio', 'fechadecompra', 'cantidad', 'ultimoproveedor', 'ultimocomprador']

class InventarioDelete(DeleteView):

      model = Inventario
      success_url = '/inventario/list'