from django.shortcuts import render


def homePage(request):
    # template variable
    context = {
        'title' : 'Home Page',
        'content' : 'This is the Home Page of the Website',
    }
    return render(request,"index.html",context)

