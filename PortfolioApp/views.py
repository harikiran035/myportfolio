from django.shortcuts import render

# Create your views here.
def display_header(request):
    return render(request, 'PortfolioApp/index.html')
