from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # post/<int:pk>/ = URLパターンを指定しています。
    # <int:pk>Djangoは整数の値を期待し、その値がpkという名前の変数でビューに渡されることを意味しています。

]