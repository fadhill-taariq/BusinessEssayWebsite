from django.urls import path
from . import views

urlpatterns = [
    path('point3/', views.index, name='point3'),
]