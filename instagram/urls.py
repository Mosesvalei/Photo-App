"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path,include
from photoapp import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('reset_passwrord/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='reset-password'),
    path('reset_password/successful', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_successful.html'), name='reset-password-successful'),
    path('register/', user_views.register, name='register-users'),
    path('profile/', user_views.profile, name='profile'),
    path('', include('gram.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
    
if settings.DEBUG:
    urlpatterns+= static(
    settings.STATIC_URL, 
    document_root = settings.STATIC_ROOT)   


