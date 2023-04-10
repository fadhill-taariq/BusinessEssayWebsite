from django.urls import path
from . import views

urlpatterns = [
    path('point2/', views.index, name='point2'),
]