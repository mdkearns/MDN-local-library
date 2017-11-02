"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

#-1- Forward requests with pattern 'catalog/' to module catalog.urls
#-2- Redirect the base URL of our application to 'catalog/'          
#-3- Enable the serving of static files during development  
          
urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'^catalog/', include('catalog.urls')),                        #-1-
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)), #-2-
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    #-3-

