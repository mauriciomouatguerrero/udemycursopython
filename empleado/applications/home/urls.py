
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('listado/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
]