from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import permission_required

def register(request):
    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'first_name', 'last_name')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group_name = request.POST.get('group')
            if group_name:
                user.groups.add('group_name')
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@permission_required('usuarios.view_ventas', raise_exception=True)
def view_ventas(request):
    # Lógica para ver ventas
    return render(request, 'ventas.html', {'title': 'Ventas'})

@permission_required('usuarios.view_compras', raise_exception=True)
def view_compras(request):
    # Lógica para ver ventas
    return render(request, 'compras.html', {'title': 'Compras'})

@permission_required('usuarios.view_inventarios', raise_exception=True)
def view_inventarios(request):
    # Lógica para ver ventas
    return render(request, 'invetarios.html', {'title': 'Inventario'})

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def logout_view(request):
    logout(request)
    return redirect('login')