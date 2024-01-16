"""
URL configuration for mygram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from feed.views import FeedView, PostCreateView, post_like_view
from accounts.views import UserRegisterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', FeedView.as_view(), name='feed'),
    path('sign_up/', UserRegisterView.as_view()),
    path('like/<int:post_pk>/', post_like_view, name='like_post')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
