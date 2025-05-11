from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LabResult(models.Model):
    Batch_ID                = models.CharField(verbose_name="ID",max_length=100,unique=True,null=True, blank=True,)
    Prep_By	                = models.CharField(max_length = 10, verbose_name="Batch ID",null=True, blank=True)
    Prep_Analysis_Method    = models.CharField(max_length = 10, verbose_name="Prep by (init)",null=True, blank=True)
    Prep_Analysis_Date      = models.DateField(("Prep/Analysis Date"), blank=True, null=True)
    Prep_Analysis_Time      = models.TimeField(("Prep/ANalysis Time"), blank=True, null=True)

    ICB_MB 	                = models.CharField(max_length = 10, verbose_name="ICB MB-",null=True, blank=True)
    ICB_MB_Dilution_Factor  = models.FloatField("ICB MB Dilution Factor (post color dev)")
    ICB_MB_Sulfide_mg_L	    = models.FloatField("ICB MB Sulfide MG/L")
    ICB_MB_Recovery_percent	= models.FloatField("ICB MB Recovery%")

    LCS	                    = models.CharField(max_length = 10, verbose_name="LCS-",null=True, blank=True)
    LCS_Dilution_Factor	    = models.FloatField("LCS Dilution Factor (post color dev)")
    LCS_Sulfide_mg_L	    = models.FloatField("LCS Sulfide MG/L")
    LCS_Recovery_percent    = models.FloatField("LCS Recovery%")

    LCSD	                = models.CharField(max_length = 10, verbose_name="LCSD-",null=True, blank=True)
    LCSD_Dilution_Factor    = models.FloatField("LCSD Dilution Factor (post color dev)")
    LCSD_Sulfide_mg_L	    = models.FloatField("LCSD Sulfide MG/L")
    LCSD_Recovery_percent   = models.FloatField("LCSD Recovery%")

    MS		                = models.CharField(max_length = 10, verbose_name="MS-",null=True, blank=True)
    MS_Dilution_Factor	    = models.FloatField("MS Dilution Factor (post color dev)")
    MS_Sulfide_mg_L	        = models.FloatField("MS Sulfide MG/L")
    MS_Recovery_percent	    = models.FloatField("MS Recovery%")

    MSD	                    = models.CharField(max_length = 10, verbose_name="MSD-",null=True, blank=True)
    MSD_Dilution_Factor	    = models.FloatField("MSD Dilution Factor (post color dev)")
    MSD_Sulfide_mg_L	    = models.FloatField("MSD Sulfide MG/L")
    MSD_Recovery_percent    = models.FloatField("MSD Recovery%")
    
    Lab_Sample_1	        = models.CharField(max_length = 10, verbose_name="Lab Sample 1",null=True, blank=True)
    LS1_Dilution_Factor	    = models.FloatField("LS1 Dilution Factor (post color dev)",null=True, blank=True)
    LS1_Sulfide_mg_L        = models.FloatField("LS1 Sulfide MG/L",null=True, blank=True)
    
    def __str__(self):
        # Display the CSV ID in the admin dropdowns and changelist:
        return self.Batch_ID
    
    class Meta:
        verbose_name = "Inorganics Sulfide"
        verbose_name_plural = "Inorganics Sulfide"

#a couple of things to note that are possible with this 
	



        
    
    