from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='myhomepage'),
    path('login/', views.login, name='loginpage'),
    path('services/', views.services, name='servicespage'),
    path('about_us/', views.about_us, name='aboutuspage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/', views.courses, name='coursespage'),
    path('addClient',views.addClient, name='addingClient'),
    path('editClient/<id>', views.editClient, name='editClient'),
    path('deleteClient/<id>', views.deleteClient, name='deleteClient'),
    path('updateClient/<id>', views.updateClient, name='updatingClient')


]