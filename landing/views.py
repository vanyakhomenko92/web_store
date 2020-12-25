from django.shortcuts import render


def landing(request):
    name = 'Vanya Khomenko'
    return render(request, 'landing/landing.html', locals())