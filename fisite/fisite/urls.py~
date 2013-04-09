from django.conf.urls import patterns, include, url
from .views import hello, current_datetime, hours_ahead, search_form, search, contact
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                      ('^hello/$', hello),
                      (r'^admin/', include(admin.site.urls)),
                      ('^search-form/$', search_form),
                      ('^search/$', search),
                      ('^tbkitemlist/$', tbkitemlist),
                      ('^contact/$', contact),
                      ('^time/$', current_datetime),
                      (r'^time/plus/(\d{1,2})/$', hours_ahead),

                       # Examples:ok ,it's my fault
                       # url(r'^$', 'todos.views.home', name='home'),
                       # url(r'^todos/', include('todos.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/',
                       # include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                       )
