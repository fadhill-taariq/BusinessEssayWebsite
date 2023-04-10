from django.urls import path
from . import views

urlpatterns = [
    path('point1/', views.index, name='point1'),
]