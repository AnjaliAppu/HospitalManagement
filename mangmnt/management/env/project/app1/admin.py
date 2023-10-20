from django.contrib import admin
from .models import Patient,Doctor,PatientAppointment,Login,AdminMaster,DepartmentSection,DiseaseList

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PatientAppointment)
admin.site.register(Login)
admin.site.register(AdminMaster)
admin.site.register(DepartmentSection)
admin.site.register(DiseaseList)

