from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'conditions.html',d)
