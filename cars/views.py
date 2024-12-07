from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def search(request):
    return render(request,'search.html')

from django.shortcuts import render
from .models import Cars

def searchBar(request):
    query = request.GET.get('query')
    if query:
        cars = Cars.objects.filter(name__icontains=query)
    results = Cars.objects.filter(field_name__icontains=query)
    return render(request, 'search_results.html', {'results': results})


# Create your views here.
