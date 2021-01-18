from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name = 'index_url'),
    path('search/', SearchField.as_view(), name='search_url'),

]
