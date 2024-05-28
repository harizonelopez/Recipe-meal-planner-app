"""
URL configuration for myblog_project project.

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
from recipe import views as recipe_views 
from recipe.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('recipe/', include('recipe.urls')),

    # user urls
    path('register/', recipe_views.register, name='register'),
    path('login/', recipe_views.login_view, name='login'), 
    path('logout/', recipe_views.logout_view, name='logout'),
    path('recipe/new/', recipe_views.recipe_new, name='recipe_new'),
    path('recipe/<int:pk>/edit/', recipe_views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/', recipe_views.recipe_delete, name='recipe_delete'),
    path('generate_pdf/', recipe_views.generate_pdf, name='generate_pdf'),

]

