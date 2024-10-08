"""schedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core import views
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', views.event_list),
    path('schedule/list/<int:id_user>/', views.json_event_list),
    path('schedule/event/', views.event),
    path('schedule/event/submit', views.submit_event), # create route for event submit
    path('schedule/event/delete/<int:id_event>/', views.delete_event), # create route for event exclusion
    # path('', views.index) # redirect to the initial page called index
    path('', RedirectView.as_view(url='/schedule/')), # other way to redirect to the initial page
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]
