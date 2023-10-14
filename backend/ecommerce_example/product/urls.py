from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='view_book'),
    path('view-product/<int:pk>/', view_product, name='view_book'),

]