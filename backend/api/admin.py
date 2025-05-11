from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import LabResult
from .resources import LabResource

@admin.register(LabResult)
class LabAdmin(ImportExportModelAdmin):
    resource_class = LabResource
    list_display = ("Batch_ID","Prep_By","Prep_Analysis_Method","Prep_Analysis_Date","Prep_Analysis_Time")