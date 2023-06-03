from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all, name="show_all"),
    path('1/', views.show_item, name="show_item"),
]
