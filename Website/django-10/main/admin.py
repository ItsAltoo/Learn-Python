from django.contrib import admin
from .models import Employe


# Register your models here.
class MemberKaryawan(admin.ModelAdmin):
    list_display = ("nama", "umur")


admin.site.register(Employe, MemberKaryawan)
