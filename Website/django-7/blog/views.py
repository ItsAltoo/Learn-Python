from django.shortcuts import render
from .forms import MahasiswaForm
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

def addMahasiswa(request):
    form = MahasiswaForm()
    if request.method == 'POST':
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            form.save()
    mhs = Mahasiswa.objects.all()
    context = {
        'title':'Add Mahasiswa',
        'heading':'Add Mahasiswa',
        'form': form,
        'mhs': mhs,
    }
    return render(request,'blog/index.html',context)