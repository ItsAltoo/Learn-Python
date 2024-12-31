from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul': "Contact Me..📞",
        'subjudul' : 'This My Contact Page..',
        'list' : [
            ['/','Home'],
            ['/about','About'],
            ['/contact','Contact']
        ],
        'banner':'contact/img/contact.png'
    }
    return render(request,'index.html',context)