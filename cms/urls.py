from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('edit-task/<slug:pk>/', edit_task_view, name='edit_task'),
    path('task/<slug:pk>/', task_view, name='task'),
    path('ready/', ready_view, name='ready'),
    path('not-ready/', not_ready_view, name='not_ready'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
