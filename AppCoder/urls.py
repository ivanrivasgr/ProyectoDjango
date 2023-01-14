from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('CargaCompra', views.CargaCompra, name="CargaCompra"),
    path('CargaVehiculo', views.CargaVehiculo, name="CargaVehiculo"),
    path('CargaEmpleado', views.CargaEmpleado, name="CargaEmpleado"),
    path('CargaItem', views.CargaItem, name="CargaItem"),
    path('BusquedaVehiculo', views.busquedaVehiculo, name = 'BusquedaVehiculo'),
    path('BusquedaCompra', views.BusquedaCompras, name = 'BusquedaCompra'),
    path('BusquedaEmpleado', views.busquedaEmpleado, name = 'BusquedaEmpleado'),
    path('BusquedaItem', views.busquedaItem, name = 'BusquedaItem'),
    path('buscarVehiculo/', views.BuscarVehiculo),
    path('BuscarCompra/', views.BuscarCompra),
    path('BuscarEmpleado/', views.BuscarEmpleado),
    path('BuscarItem/', views.BuscarItem),

    ######      CBV       #######

    path('vehiculos/list', views.TallerList.as_view(), name = 'ListVeh'),
    path(r'^vehiculo/(?P<pk>\d+)$', views.TallerDetalle.as_view(), name = 'DetalleVeh'),
    path(r'^nuevoVeh$', views.TallerCreate.as_view(), name = 'CreateVeh'),
    path(r'^editarVeh/(?P<pk>\d+)$', views.TallerUpdate.as_view(), name = 'UpdateVeh'),
    path(r'^borrarVeh/(?P<pk>\d+)$', views.TallerDelete.as_view(), name = 'DeleteVeh'),

    path('compra/list', views.ComprasList.as_view(), name = 'ListCompra'),
    path(r'^compra/(?P<pk>\d+)$', views.ComprasDetalle.as_view(), name = 'DetalleCompra'),
    path(r'^nuevaCompra$', views.ComprasCreate.as_view(), name = 'CreateCompra'),
    path(r'^editarCompra/(?P<pk>\d+)$', views.ComprasUpdate.as_view(), name = 'UpdateCompra'),
    path(r'^borrarCompra/(?P<pk>\d+)$', views.ComprasDelete.as_view(), name = 'DeleteCompra'),

    path('empleado/list', views.RRHHList.as_view(), name = 'ListEmpleado'),
    path(r'^empleado/(?P<pk>\d+)$', views.RRHHDetalle.as_view(), name = 'DetalleEmpleado'),
    path(r'^nuevoEm$', views.RRHHCreate.as_view(), name = 'CreateEmpleado'),
    path(r'^editarEm/(?P<pk>\d+)$', views.RRHHUpdate.as_view(), name = 'UpdateEmpleado'),
    path(r'^borrarEm/(?P<pk>\d+)$', views.RRHHDelete.as_view(), name = 'DeleteEmpleado'),

    path('item/list', views.InventarioList.as_view(), name = 'ListItem'),
    path(r'^item/(?P<pk>\d+)$', views.InventarioDetalle.as_view(), name = 'DetalleItem'),
    path(r'^nuevoIt$', views.InventarioCreate.as_view(), name = 'CreateItem'),
    path(r'^editarIt/(?P<pk>\d+)$', views.InventarioUpdate.as_view(), name = 'UpdateItem'),
    path(r'^borrarIt/(?P<pk>\d+)$', views.InventarioDelete.as_view(), name = 'DeleteItem')

]


