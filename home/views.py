from django.shortcuts import render


def home_(request):
    return render(request, "index.html")
