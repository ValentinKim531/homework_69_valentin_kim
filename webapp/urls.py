from django.urls import path

from webapp.views.task_1_and_2 import add, subtract, multiply, divide, get_token_view, IndexView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("add/", add, name='add'),
    path("subtract/", subtract, name='subtract'),
    path("multiply/", multiply, name='multiply'),
    path("divide/", divide, name='divide'),
    path('token/', get_token_view, name='token'),
]