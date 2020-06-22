from django.urls import path
from .views import index, contato, produto

urlpatterns = [

    # O Vazio ali é a raiz, passamos o template, o nome da rota logo em seguida

    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
]
