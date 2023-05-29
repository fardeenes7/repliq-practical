from django.db import models

# Create your models here.

class AssetType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Asset Types"
    
    def __str__(self):
        return self.name
    

class Asset(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    asset_type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Assets"
    
    def __str__(self):
        return self.name
    

class AssetDelegation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey('company.User', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    class Meta:
        verbose_name_plural = "Asset Delegations"
    
    def __str__(self):
        return self.asset.name + " - " + self.employee.username