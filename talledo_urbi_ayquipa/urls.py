
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name = "index"),
    path('cursos/', views.cursos, name = "cursos"),
    path('crear_curso/', views.crear_curso, name = "crear_curso"),
    path('carreras/', views.carreras, name = "carreras"),
    path('crear_carrera/', views.crear_carrera, name ="crear carrera")
]
