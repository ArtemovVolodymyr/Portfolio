# About_Me.urls

from django.urls import path

from . import views

urlpatterns = [
    path('about_me/', views.about_me_page, name='about_me_page'),
]
