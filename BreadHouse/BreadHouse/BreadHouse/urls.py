from django.contrib import admin
from django.urls import path
from django.urls import include





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Menue.urls')),
    path('',include('django.contrib.auth.urls')),
    
   
    
]
