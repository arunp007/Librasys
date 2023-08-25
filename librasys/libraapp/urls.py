from django.urls import path
from.import views

urlpatterns = [
    path('user_home', views.user_home, name = 'user_home'),
    path('user_login', views.user_login, name = 'user_login'),
    path('user_logout', views.user_logout, name = 'user_logout'),
    path('user_signup', views.user_signup, name = 'user_signup'),
    path('user_table', views.user_table, name = 'user_table'),
    path('user_delete\<int:id>', views.user_delete, name = 'user_delete'),
    path('user_update\<int:id>', views.user_update, name = 'user_update'),
    path('librarian_home', views.librarian_home, name = 'librarian_home'),
    path('librarian_login', views.librarian_login, name = 'librarian_login'),
    path('librarian_logout', views.librarian_logout, name = 'librarian_logout'),
    path('librarian_signup', views.librarian_signup, name = 'librarian_signup'),
    path('librarian_table', views.librarian_table, name = 'librarian_table'),
    path('librarian_delete\<int:id>', views.librarian_delete, name = 'librarian_delete'),
    path('librarian_update\<int:id>', views.librarian_update, name = 'librarian_update'),
    path('admin_home', views.admin_home, name = 'admin_home'),
    path('admin_login', views.admin_login, name = 'admin_login'),
    path('admin_signup', views.admin_signup, name = 'admin_signup'),
    path('admin_table', views.admin_table, name = 'admin_table'),
    path('admin_delete\<int:id>', views.admin_delete, name = 'admin_delete'),
    path('admin_update\<int:id>', views.admin_update, name = 'admin_update'),
    path('admin_logout', views.admin_logout, name = 'admin_logout'),
]