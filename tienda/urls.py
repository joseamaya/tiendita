from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

from django_project import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tienda.views.home', name='home'),
    # url(r'^tienda/', include('tienda.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^facturacion/', include('facturacion.urls',namespace='facturacion')),
    url(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
