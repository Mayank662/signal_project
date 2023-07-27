from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun1),
    path('create-model1/',views.create_model1)
]