from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from facturacion.views import factura, guardarFactura,BusquedaCliente,BusquedaProducto, NuevoCliente, Clientes, Productos,DetalleCliente, DetalleProducto

urlpatterns = patterns('',
	url(r'^$',factura, name="factura"),
	url(r'^guardarFactura/$',guardarFactura, name="guardarFactura"),
	url(r'^busquedaCliente/$',BusquedaCliente.as_view(), name="busquedaCliente"),
	url(r'^busquedaProducto/$',BusquedaProducto.as_view(), name="busquedaProducto"),
	url(r'^nuevoCliente/$',NuevoCliente.as_view(), name="nuevoCliente"),
	url(r'^clientes/$',Clientes.as_view(), name="clientes"),
	url(r'^productos/$',Productos.as_view(), name="productos"),
	url(r'^cliente/(?P<pk>\d+)/$',DetalleCliente.as_view(), name="cliente"),
	url(r'^producto/(?P<pk>\d+)/$',DetalleProducto.as_view(), name="producto"),
	#url(r'^(?P<encuesta_id>\d+)/$',views.detalle, name='detalle'),
	#url(r'^(?P<encuesta_id>\d+)/resultados/$',views.resultados, name='resultados'),
	#url(r'^(?P<encuesta_id>\d+)/voto/$',views.voto, name='voto'),
)
if not settings.DEBUG:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
		)