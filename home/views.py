from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    #return HttpResponse('this is tushar project')

def contact(request):
    return render(request, 'contact.html')




