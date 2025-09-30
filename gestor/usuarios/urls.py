from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Cambiado de 'home' a login_view
    path('register/', views.register, name='register'),  # aquí se define 'home'
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('ventas/', views.view_ventas, name='ventas'),
    path('compras/', views.view_compras, name='compras'),
    path('inventarios/', views.view_inventarios, name='inventarios'),
]