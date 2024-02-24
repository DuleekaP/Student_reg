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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-user-view-billing - 2/', TemplateView.as_view(template_name='cmb_Reg/app-user-view-billing - cmb - 2.html'), name='app-user-view-billing - 2'),
    path('app-user-view-billing/', TemplateView.as_view(template_name='cmb_Reg/app-user-view-billing - cmb.html'), name='app-user-view-billing'),
    path('app-user-view-billing - 3/', TemplateView.as_view(template_name='cmb_Reg/app-user-view-billing - cmb - 3.html'), name='app-user-view-billing - 3'),
    path('app-user-view-billing - 4/', TemplateView.as_view(template_name='cmb_Reg/app-user-view-billing - cmb - 4.html'), name='app-user-view-billing - 4'),
    path('app-user-view-billing - 5/', TemplateView.as_view(template_name='cmb_Reg/app-user-view-billing - cmb - 5.html'), name='app-user-view-billing - 5'),
    path('auth-forgot-password-basic-cmb/', TemplateView.as_view(template_name='cmb_Reg/auth-forgot-password-basic-cmb.html'), name='auth-forgot-password-basic-cmb'),
    path('auth-login-basic - cmb/', TemplateView.as_view(template_name='cmb_Reg/auth-login-basic - cmb.html'), name='auth-login-basic - cmb'),
    path('auth-register-basic - cmb/', TemplateView.as_view(template_name='cmb_Reg/auth-register-basic - cmb.html'), name='auth-register-basic - cmb'),
    path('form-wizard-icons - cmb/', TemplateView.as_view(template_name='cmb_Reg/form-wizard-icons - cmb.html'), name='form-wizard-icons - cmb'),
]

# Append static URL pattern for development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
