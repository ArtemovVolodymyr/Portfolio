# achive.views
from django.shortcuts import render

# Create your views here.
def achive_page(request):
    return render(request, 'Achive/index_achive.html')