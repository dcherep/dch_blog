from django.shortcuts import render, redirect
from .models import User,Role
from .forms import UserForm,RoleForm

def users(request):
    users=User.objects.all()
    return render(request, 'users.html', {'users': users})

def add_user(request):
    if request.method=="POST":
        user=UserForm(request.POST)
        if user.is_valid():
            user.save()
        return redirect('/users/')
    else:
        form=UserForm()
        return render(request, "add_user.html",{'form': form})

def roles(request):
    roles=Role.objects.all()
    return render(request, 'roles.html', {'roles': roles})

def add_role(request):
    if request.method=="POST":
        role=RoleForm(request.POST)
        if role.is_valid():
            role.save()
        return redirect('/roles/')
    else:
        form=RoleForm()
        return render(request, "add_role.html",{'form': form})
    
def edit_user(request,id_user):
    user=User.objects.get(id=id_user)
    if request.method=="POST":
        user=UserForm(request.POST,instance=user)
        if user.is_valid():
            user.save()
        return redirect('/users/')
    else:
        userform=UserForm(instance=user)
    return render(request, 'updateUser.html', {'form': userform})

def deleteUser(request, id_user):
    users=User.objects.get(id=id_user)
    users.delete()
    return redirect('/users/')

def edit_role(request,id_role):
    role=Role.objects.get(id=id_role)
    if request.method=="POST":
        role=RoleForm(request.POST,instance=role)
        if role.is_valid():
            role.save()
        return redirect('/roles/')
    else:
        roleform=RoleForm(instance=role)
    return render(request, 'updateRole.html', {'form': roleform})

def deleteRole(request, id_role):
    roles=Role.objects.get(id=id_role)
    roles.delete()
    return redirect('/roles/')


