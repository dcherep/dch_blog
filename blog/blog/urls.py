
#from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('add_user/', views.add_user),
    path('users/', views.users),
]
