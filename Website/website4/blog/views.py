from django.shortcuts import render

# Create your views here.
def blogPage(request):
    context = {
        "title":"Blog Page",
        "content":"This is the blog page"
    }
    return render(request,"blog/index.html",context)