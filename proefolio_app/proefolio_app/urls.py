# proefolio_app.urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('', include('About_Me.urls')),
    path('', include('Achive.urls')),
    path('', include('CV.urls')),

]
