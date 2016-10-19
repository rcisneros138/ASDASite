from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'ASDAWebApp/home.html')

def contact(request):
    return render(request, 'ASDAWebApp/basic.html', {'content': ['if you want to contact, email me at',
                                                                 'rcisneros138@gmail.com']})


