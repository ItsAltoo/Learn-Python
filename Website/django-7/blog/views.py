from django.shortcuts import render

from .models import Mahasiswa
# Create your views here.


def index(request):
    mhs = Mahasiswa.objects.all()
    context = {
        'title':'Welcome',
        'heading':'This Test Website',
        'mahasiswa': mhs,
    }
    return render(request,'blog/index.html',context)