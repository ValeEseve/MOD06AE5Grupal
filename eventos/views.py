from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    return render(request, 'login_page.html')

def register_view(request):
    return render(request, 'register_page.html')

def add_evento(request):
    return render(request, 'add_event.html')

def home(request):
    return render(request, 'home.html')