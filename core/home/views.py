from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):

    peoples = [
        {'name' : 'chirag lamba', 'age' : 25},
        {'name' : 'thor ', 'age' : 6},
        {'name' : 'bruce banner', 'age' : 28},
        {'name' : 'tony stark', 'age' : 2},
    ]
    
    for people in peoples:
        print(peoples)
    
    return render(request, "index.html", context = {'peoples': peoples})

def contact(request):
    return render(request, "contact.html")
def about(request):   
    return render(request, "about.html")




def success_page(request):
    return HttpResponse("<h2>this is a success page</h2>")
