from django.shortcuts import render

def index(request):
    context = {
        'judul':'Welcome to my website 🫠',
        'subjudul':'This my Home Page',
        'list':[
            ['/','Home'],
            ['/about','About'],
            ['/contact','Contact']
        ]
    }
    return render(request,'index.html',context)