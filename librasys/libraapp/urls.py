from django.urls import path
from.import views

urlpatterns = [
    path('user_home', views.user_home, name = 'user_home'),
    path('user_login', views.user_login, name = 'user_login'),
    path('user_signup', views.user_signup, name = 'user_signup'),
    path('librarian_home', views.librarian_home, name = 'librarian_home'),
    path('librarian_login', views.librarian_login, name = 'librarian_login'),
    path('librarian_signup', views.librarian_signup, name = 'librarian_signup'),
    path('admin_home', views.admin_home, name = 'admin_home'),
    path('admin_login', views.admin_login, name = 'admin_login'),
    path('admin_signup', views.admin_signup, name = 'admin_signup'),
]