from django.shortcuts import render

def home_page_view(request):
    return render(request, 'index.html')

def _404_page_view(request):
    return render(request, '404.html')

def success_page_view(request):
    return render(request, 'success/success.html')
