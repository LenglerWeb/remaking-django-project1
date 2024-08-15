from recipes.views import home, sobre, contato
from django.urls import path

urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # Sobre
    path('contato/', contato),  # Contato
]
