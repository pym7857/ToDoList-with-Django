from django.urls import path
from django.urls.resolvers import URLPattern
from . import views 

urlpatterns = [
    path('', views.index, name='index'), # views.py의 def index()
    path('createTodo/', views.createTodo, name='createTodo'),
    path('doneTodo/', views.doneTodo, name='doneTodo')
]

