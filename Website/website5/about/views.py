from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul': 'About Me..🤓',
        'subjudul' : 'This About Me..',
        'list':[
            ['/','Home'],
            ['/about','About'],
            ['/contact','Contact']
        ]
    }
    return  render(request,'about/index.html',context)