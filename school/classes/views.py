from django.http import HttpResponse


from django.shortcuts import render

# Create your views here.
#where all functions are created

def home(request):
    context = {'navbar':'home'}
    return render(request, 'home.html', context)

def about(request):
    return render(request,'about.html', {'navbar':'about'})

def contact(request):
    return render(request, 'pages/contact.html',{'navbar':'contact'} )


def add(request):
    return render(request, 'add.html', {'navbar':'add '})

def viewdata(request):
    return render(request, 'viewdata.html', {'navbar':'viewdata'})