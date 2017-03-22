"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from learn import views as learn_views
from marcgis import views as marcgis_views
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', learn_views.home, name='home'),
    url(r'^marcgis/$', marcgis_views.index, name='marcgis'),
    url(r'^marcgis/demo/$', marcgis_views.demo, name='soshinesee'),
    url(r'^marcgis/alpha/$', marcgis_views.alpha, name='soshinesee_alpha'),
    url(r'^marcgis/alpha_blockdata/$', marcgis_views.alpha_blockdata, name='soshinesee_alpha_blockdata'),
    url(r'^marcgis/alpha_radius/$', marcgis_views.alpha_radius, name='soshinesee_alpha_radius'),


]
