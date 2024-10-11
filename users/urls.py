from django.urls import path

from users.views import login_view, register_view, profile_view, verify_email, logout_view, user_update_view

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('verify-email/<uidb64>/<token>', verify_email, name='verify_email'),
    path('update/', user_update_view, name='update'),
]
