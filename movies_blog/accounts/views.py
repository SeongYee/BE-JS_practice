from django.shortcuts import render

def index(request):
    return render(request, 'accounts/index.html')
# Create your views here.

