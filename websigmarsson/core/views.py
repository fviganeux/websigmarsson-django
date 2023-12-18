from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def tutoriales(request):
    return render(request, "core/tutoriales.html")

def livros(request):
    return render(request, "core/livros.html")

def offtopic(request):
    return render(request, "core/offtopic.html")

def servicios(request):
    return render(request, "core/servicios.html")

def contacto(request):
    return render(request, "core/contacto.html")