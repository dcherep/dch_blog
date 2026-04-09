
#from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('add_user/', views.add_user),
    path('users/', views.users),
    path('add_role/', views.add_role),
    path('roles/', views.roles),
    path('edituser/<int:id_user>', views.edit_user),
    path('deleteuser/<int:id_user>', views.deleteUser),
    path('editrole/<int:id_role>', views.edit_role),
    path('deleterole/<int:id_role>', views.deleteRole),
]
