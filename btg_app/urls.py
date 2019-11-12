
from django.urls import path, include
from btg_app import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]