"""
URL configuration for hotel project.

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
from django.urls import path,include
from survey import urls as surv_url
from survey import views as surv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(surv_url)),
    path('register/', surv.register, name='register'),
    path('login/', surv.LoginPage, name='login'),
    path('logout/', surv.LogoutUser, name='logout'),
    path('', surv.Home, name='home'),
    path('survey/', surv.Surveypage, name='survey'),
    path('project/', surv.ProjPage, name='project'),
    path('proview/<str:pk>/', surv.ProView, name='proview'),
    path('projectform/<str:pk>/', surv.ProjFIl, name='projectform'),
    path('delete/<str:pk>/', surv.DeleteProj, name='delete'),

]
