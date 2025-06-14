from django.urls import path
from .views import register_view, home, add_word
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),  # root URL login sayfası
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # istersen bunu kaldırabilirsin, kök zaten login yapıyor
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', home, name='home'),
    path('add_word/', add_word, name='add_word'),
]