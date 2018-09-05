import authapp.views as authapp
from django.urls import path

app_name = 'authapp'

urlpatterns = [
    path('login/ru', authapp.login, name='login'),
    path('logout/ru', authapp.logout, name='logout'),
    path('register/ru', authapp.register, name='register'),
    path('edit/ru', authapp.edit, name='edit'),
    path('login/', authapp.login_eng, name='login_eng'),
    path('logout/', authapp.logout_eng, name='logout_eng'),
    path('register/', authapp.register_eng, name='register_eng'),
    path('edit/', authapp.edit_eng, name='edit_eng'),
]