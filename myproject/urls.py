
from django.contrib import admin
from django.urls import path, include
import core.urls 
import user.urls 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include(core.urls, namespace="core")),
    path('user/',  include(user.urls, namespace="user")),
    
    
    
]
