from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import Mahasiswa

# Create your views here.
def addMahasiswa(request):
    errors = []
    if request.method == "POST":
        name_mhs = request.POST.get('mhs_name')
        nim_mhs = request.POST.get('mhs_nim')
        bio_mhs = request.POST.get('mhs_bio')
        
        if not name_mhs:
            errors.append("Name is required.")
        if not nim_mhs:
            errors.append("NIM is required.")
        if not bio_mhs:
            errors.append("Bio is required.")
        
        if not errors:
            try:
                maha = Mahasiswa(nama=name_mhs, nim=nim_mhs, bio=bio_mhs)
                maha.save()
                return redirect('addMahasiswa')
            except IntegrityError:
                errors.append("NIM must be unique.")
    
    context = {
        'title': 'Add Mahasiswa',
        'mhs': Mahasiswa.objects.all(),
        'errors': errors,
    }
    return render(request, 'blog/index.html', context)

def deleteMahasiswa(request, id):
    maha = get_object_or_404(Mahasiswa, id=id)
    maha.delete()
    return redirect('addMahasiswa')

# def secondPage(request):
#     return render(request,"blog/test.html")