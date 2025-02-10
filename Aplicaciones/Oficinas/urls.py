#URLS especificas de la aplicacion
from django.urls import path

from.import views

urlpatterns = [

    path('',views.inicio),
    path('inicio/', views.inicio),
    path('nueva_oficina/', views.nueva_oficina),
    path('listado_oficinas/', views.listado_oficinas),
    path('guardar_oficina/', views.guardar_oficina),
    path('eliminar_oficina/<int:id>/', views.eliminar_oficina),
    path('editar_oficina/<int:id>/', views.editar_oficina),
    path('procesar_editar_oficina/', views.procesar_editar_oficina),



    path('nuevo_contratista/', views.nuevo_contratista),
    path('listado_contratistas/', views.listado_contratistas),
    path('guardar_contratista/', views.guardar_contratista),
    path('eliminar_contratista/<int:id>/', views.eliminar_contratista),
    path('editar_contratista/<int:id>/', views.editar_contratista),
    path('procesar_editar_contratista/', views.procesar_editar_contratista),





    path('nueva_reforma/', views.nueva_reforma),
    path('listado_reformas/', views.listado_reformas),
    path('guardar_reforma/', views.guardar_reforma),
    path('eliminar_reforma/<int:id>/', views.eliminar_reforma),
    path('editar_reforma/<int:id>/', views.editar_reforma),
    path('procesar_editar_reforma/', views.procesar_editar_reforma),


    


    path('nuevo_suministro/', views.nuevo_suministro),
    path('listado_suministros/', views.listado_suministros),
    path('guardar_suministro/', views.guardar_suministro),
    path('eliminar_suministro/<int:id>/', views.eliminar_suministro),
    path('editar_suministro/<int:id>/', views.editar_suministro),
    path('procesar_editar_suministro/', views.procesar_editar_suministro),


    path('nuevo_reforma_suministro/', views.nuevo_reforma_suministro),
    path('listado_reforma_suministro/', views.listado_reforma_suministro),
    path('guardar_reforma_suministro/', views.guardar_reforma_suministro),
    path('eliminar_reforma_suministro/<int:id>/', views.eliminar_reforma_suministro),
    path('editar_reforma_suministro/<int:id>/', views.editar_reforma_suministro),
    path('procesar_editar_reforma_suministro/', views.procesar_editar_reforma_suministro),



    path('generar_reporte_pdf/', views.generar_reporte_pdf, name='generar_reporte_pdf'),


]




