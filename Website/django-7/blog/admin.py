from django.contrib import admin
from .models import Mahasiswa

# Register your models here.

class MemberMahasiswa(admin.ModelAdmin):
    list_display = ('nama','nim',)

admin.site.register(Mahasiswa,MemberMahasiswa)