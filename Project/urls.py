"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from member.views import register_view,login_view,logout_view,transient_view,plot1_view
from Main.views import home_screen_view
from supply.views import supply_view
from demand.views import demand_view
urlpatterns = [
    path('',home_screen_view,name='home'),
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('transient/',transient_view,name='transient'),
    path('supply/',supply_view,name='supply'),
    path('demand/',demand_view,name='demand'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)