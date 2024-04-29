# cv.views
from django.shortcuts import render

# Create your views here.
def cv_page(request):
    return render(request, 'CV/index_cv.html')