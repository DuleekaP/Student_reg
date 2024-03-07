"""
URL configuration for AP_project project.

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
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from cmb_Reg import views  #this might cause troubles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth-forgot-password-basic-cmb/', TemplateView.as_view(template_name='cmb_Reg/auth-forgot-password-basic-cmb.html'), name='auth-forgot-password-basic-cmb'),
    path('auth-login-basic - cmb/', TemplateView.as_view(template_name='cmb_Reg/auth-login-basic - cmb.html'), name='auth-login-basic - cmb'),
    path('auth-register-basic - cmb/', TemplateView.as_view(template_name='cmb_Reg/auth-register-basic - cmb.html'), name='auth-register-basic - cmb'),
    path('form-wizard-icons - cmb/', TemplateView.as_view(template_name='cmb_Reg/form-wizard-icons - cmb.html'), name='form-wizard-icons - cmb'),
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/',views.user_details, name='profile'),
    path('education/', views.user_qualification, name='education'),
    path('employement/', views.user_employement, name='employement'),
    path('publications/', views.user_publication, name='publications'),
    path('referees/', views.user_refrees, name='referees'),
    path('apply/', views.user_application, name='apply'),
    path('allDetils/', views.user_profile, name='allDetails'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
]

# Append static URL pattern for development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
