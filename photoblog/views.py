from django.shortcuts import render

# Create your views here.


# Page Shown when not logged in
def notloggedin(request):

    return render(request, 'basics/notloggedin.html')

def home(request):
    return render(request, 'basics/home.html')