from django.shortcuts import render

def index(request):
    return render(request, 'compilais/html/index.html')

def courses(request):
    return render(request, 'compilais/html/courses.html')

def plans(request):
    return render(request, 'compilais/html/plans.html')

def dashboard(request):
    return render(request, 'compilais/html/dashboard.html')