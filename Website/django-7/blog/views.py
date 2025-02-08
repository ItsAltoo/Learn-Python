from django.shortcuts import render

from .forms import MahasiswaForm
from .models import Mahasiswa
# Create your views here.


def addMahasiswa(request):
    if request.method == "POST":
        name_mhs = request.POST['mhs_name']
        nim_mhs = request.POST['mhs_nim']
        bio_mhs = request.POST['mhs_bio']
        
        maha = Mahasiswa(nama=name_mhs,nim=nim_mhs,bio=bio_mhs)
        maha.save()
            
    context = {
        'title':'Add Mahasiswa',
        'heading':'Add Mahasiswa',
        'mhs': Mahasiswa.objects.all(),
    }
    return render(request,'blog/index.html',context)