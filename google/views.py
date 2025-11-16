from django.shortcuts import render

def google_index(request):
    return render(request, "index.html")

def google_image(request):
    return render(request, "image.html")

def google_advanced(request):
    return render(request, "advanced.html")
