
from django.urls import path
from ws import views
urlpatterns = [
    path('submit_data/', views.submit_contact, name='submit_data'),
]