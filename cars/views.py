from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def search(request):
    return render(request,'search.html')

from django.shortcuts import render
from .models import Cars

def searchBar(request):
    query = request.GET.get('search')
    if query:
        cars = Cars.objects.filter(price__contains=query)
    return render(request, 'search_results.html', {'cars': cars})



def search_view(request):
    query = request.GET.get('search',)
    results = Cars.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', { 'cars': cars})

# Create your views here.
