from import_export import resources
from .models import LabResult

class LabResource(resources.ModelResource):
    class Meta:
        model = LabResult
        # tell import-export which field to use as the unique key
        import_id_fields = ("Batch_ID",)
        # explicitly list the CSV columns you expect
        fields = ("Batch_ID", "Prep_By", "Prep_Analysis_Method", "Prep_Analysis_Date", 
                  "Prep_Analysis_Time",	"ICB_MB", "ICB_MB_Dilution_Factor",	
                  "ICB_MB_Sulfide_mg_L", "ICB_MB_Recovery_percent",	"LCS",	"LCS_Dilution_Factor",
                  "LCS_Sulfide_mg_L", "LCS_Recovery_percent", "LCSD", "LCSD_Dilution_Factor",	
                  "LCSD_Sulfide_mg_L", "LCSD_Recovery_percent",	"MS", "MS_Dilution_Factor",
                  "MS_Sulfide_mg_L", "MS_Recovery_percent",	"MSD", "MSD_Dilution_Factor",
                  "MSD_Sulfide_mg_L", "MSD_Recovery_percent", "Lab_Sample_1", "LS1_Dilution_Factor", "LS1_Sulfide_mg_L" )
        