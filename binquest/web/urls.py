from django.urls import path
from . import views





urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('loginn', views.loginn, name='loginn'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.add_todo, name='add_todo'),
    path('list/', views.todo_list, name='todo_list'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('contact/', views.contact_form, name='contact_form'),
    path('search/', views.todo_search, name='todo_search'),
    path('nonbio_search/', views.nonbio_search, name='nonbio_search'),
    path('redirect/<int:todo_id>/', views.redirect_to_location, name='redirect_to_location'),
    path('identify', views.identify, name='identify'),
    
    
]




