from django.urls import path
from . import views

urlpatterns = [
    path('conclusion/', views.index, name='conclusion'),
]