from django.urls import path
from . import views 
urlpatterns=[
    path('',views.pantalla_inicio, name='pantalla_inicio'),
    path('estados/',views.estado_list, name='estado_list'),
    path('estados/nuevo/',views.Estado_create,name='Estado_create'),
    path('estados/editar/<int:pk>/', views.estado_update, name= 'estado_update'),
    path('principal/', views.principal, name='principal'),
    path('estados/eliminar/<int:pk>/', views.estado_delete, name= 'estado_delete'),
    path('estados/municipio/',views.municipio_list, name='municipio_list'),
    path('municipio/nuevo/',views.municipio_create, name='municipio_create'),
    path('municipios/editar/<int:pk>/', views.municipio_update, name= 'municipio_update'),
    path('municipios/eliminar/<int:pk>/', views.municipio_delete, name= 'municipio_delete'),
    path('estados/municipio/colonia/',views.colonia_list, name='colonia_list'),
    path('estados/municipio/colonia/nuevo/',views.colonia_create, name='colonia_create'),
    path('estados/municipio/colonia/editar/<int:pk>/', views.colonia_update, name= 'colonia_update'),
    path('estados/municipio/colonia/eliminar/<int:pk>/', views.colonia_delete, name= 'colonia_delete'),

    

]