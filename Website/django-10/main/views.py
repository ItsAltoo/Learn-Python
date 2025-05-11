from django.shortcuts import render, redirect
from .models import Employe


# Create your views here.
def addEmploye(request):
    template_file = "index.html"

    if request.method == "POST":
        nama = request.POST.get("nama_emp")
        umur = request.POST.get("umur_emp")
        job = request.POST.get("job_emp")
        Employe.objects.create(nama=nama, umur=umur, job=job)
        return redirect("addEmploye")

    context = {"heading": "main", "karyawan": Employe.objects.all()}
    return render(request, template_file, context)

