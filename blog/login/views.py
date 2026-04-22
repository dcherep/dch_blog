from django.shortcuts import render, redirect
from .models import User,Role
from .forms import UserForm,RoleForm
from .decorators import login_required,is_director

@login_required
def for_authorized(request):
    return render(request, 'page_for_authorized.html')

@is_director
def for_director(request):
    return render(request, 'page_for_director.html')

def logout_view(request):
    request.session.flush()
    return redirect('/login')


def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        login=request.POST.get('login')
        password=request.POST.get('pas')

        try:
            user=User.objects.get(login=login)
        except User.DoesNotExist:
            return redirect('/login')
        
        if password != user.password:
            return redirect('/login')

        request.session['user_id'] = user.id
        request.session['login'] = user.login
        return redirect('/')

def index(request):
    if request.session.get('user_id'):
        l=request.session.get('login')
        return render (request, 'index.html',{'login': l})
    else:
        return redirect('/login/')

def users(request):
    if request.session.get('user_id'):
        users=User.objects.all()
        return render(request, 'users.html', {'users': users})
    else:
        return redirect('/login/')
  
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
    if request.session.get('user_id'):
        roles=Role.objects.all()
        return render(request, 'roles.html', {'roles': roles})
    else:
        return redirect('/login/')
   

def add_role(request):
    if request.session.get('user_id'):
        if request.method=="POST":
            role=RoleForm(request.POST)
            if role.is_valid():
                role.save()
            return redirect('/roles/')
        else:
            form=RoleForm()
            return render(request, "add_role.html",{'form': form})
    else:
        return redirect('/login/')
    

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


