from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.greeting),
    path('gaos', views.gaos, name='gaos'),
]
