from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name='index.html')
def about(request):
    return render(request,template_name='about.html')
def blog(request):
    return render(request,template_name='blog.html')
def coffees(request):
    return render(request,template_name='coffees.html')
def contact(request):
    return render(request,template_name='contact.html')
