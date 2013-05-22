from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Main
    url(r'^$', 'main.views.home', name='home'),

    # Apps
    # url(r'^myapp/', include("apps.myapp.urls")),

    # Plugables Apps
    url(r'^admin/', include(admin.site.urls)),
)
