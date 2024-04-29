# home_page.views

from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page/index_home.html')


