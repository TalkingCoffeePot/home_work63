from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import UserRegisterView, UserProfile, logout_view
from feed.views import PostCreateView

app_name='accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/sign_in.html'), name='log_in'),
    path('create/', UserRegisterView.as_view(), name='register_user'),
    path('profile/<int:profile_pk>', UserProfile.as_view(), name='profile'),
    path('logout/', logout_view, name='log_out'),
    path('<int:profile_pk>/new_post/', PostCreateView.as_view(), name='new_post')
]