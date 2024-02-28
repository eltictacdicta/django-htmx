from django.urls import path
from .views import *

app_name = 'paginas'
urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
]