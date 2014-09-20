from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from facturacion.views import factura, guardarFactura,BusquedaCliente,BusquedaProducto, NuevoCliente, Clientes, Productos,DetalleCliente, DetalleProducto

urlpatterns = patterns('',
	url(r'^$',factura, name="factura"),
	url(r'^guardarFactura/$',guardarFactura, name="guardarFactura"),
	url(r'^busquedaCliente/$',login_required(BusquedaCliente.as_view()), name="busquedaCliente"),
	url(r'^busquedaProducto/$',login_required(BusquedaProducto.as_view()), name="busquedaProducto"),
	url(r'^nuevoCliente/$',login_required(NuevoCliente.as_view()), name="nuevoCliente"),
	url(r'^clientes/$',login_required(Clientes.as_view()), name="clientes"),
	url(r'^productos/$',login_required(Productos.as_view()), name="productos"),
	url(r'^cliente/(?P<pk>\d+)/$',login_required(DetalleCliente.as_view()), name="cliente"),
	url(r'^producto/(?P<pk>\d+)/$',login_required(DetalleProducto.as_view()), name="producto"),
	#url(r'^(?P<encuesta_id>\d+)/$',views.detalle, name='detalle'),
	#url(r'^(?P<encuesta_id>\d+)/resultados/$',views.resultados, name='resultados'),
	#url(r'^(?P<encuesta_id>\d+)/voto/$',views.voto, name='voto'),
)