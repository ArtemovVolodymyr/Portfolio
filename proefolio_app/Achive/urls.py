# achieve.urls
from django.urls import path

from . import views

urlpatterns = [
    path('achive/', views.achive_page, name='achive_page'),
]
