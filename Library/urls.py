"""
URL configuration for Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Book.views import *
from accounts.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('' , home , name= "home"),
    path('new_book/' , new_book , name = "new_book"),
    path('login_page/' , login_page , name = "login_page") ,
    path('register_page/' , register_page , name = "register_page") ,
    path('update_book/<id>/' , update_book ,name = 'update_book'),
    path('delete_book/<id>/' , delete_book ,name = 'delete_book'),
    path('logout_page/' , logout_page , name = 'logout_page'),
    path('book_detail/<id>' , book_detail , name = 'book_detail'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT) 

urlpatterns += staticfiles_urlpatterns()    
