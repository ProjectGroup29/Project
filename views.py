from django.shortcuts import render


# Create your views here.
def home(request):
    template = 'Home/index.html'
    return render(request, template, {})