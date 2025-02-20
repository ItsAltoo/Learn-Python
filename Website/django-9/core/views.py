from django.shortcuts import render

# Create your views here.
def index(request):
    
    
    
    context = {
        'heading' : 'This Core',
        'subHeading':'Coreeeeee'
    }
    return render(request,'index.html',context)