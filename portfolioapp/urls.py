"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from portfolioapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('service/',views.service,name='service'),
    path('contect/',views.contect,name='contect'),
    path('sendmail/',views.sendmail,name='sendmail'),
    path('blog/',views.blog,name='blog'),
    path('aboutmore/',views.aboutmore,name='aboutmore'),
    path('certifications/',views.certifications,name='certifications'),
    path("aboutmore/", views.aboutmore, name="aboutmore"),
    path("Skills/", views.Skills, name="Skills"),
    path('projects/', views.projects, name='projects'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('childhood/', views.childhood, name='childhood'),
    path('download-resume/', views.download_resume, name='download_resume'),
]
