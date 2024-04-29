# About_Me.views
from django.shortcuts import render

# Create your views here.


def about_me_page(request):
    return render(request, 'About_Me/index_about_me.html')
