from myapp import views
from django.urls import path


urlpatterns = [

    path('', views.index, name='index'),
    path('mapas/',views.mapas, name="mapas"),
    path('mapa1/', views.mapa1, name='mapa1'),  # Ruta para mapa1
    path('mapa2/', views.mapa2, name='mapa2'),  # Ruta para mapa2
    path('mapa3/',views.mapa3, name='mapa3' ),  # Ruta para mapa3
    path('mas informacion/', views.mas_informacion, name= "mas_informacion"),
    path('add_marker/', views.add_marker, name='add_marker'),
]