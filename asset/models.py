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
    description = models.CharField(max_length=200, null=True, blank=True)
    asset_type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Assets"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.company = self.user.company
        super(Asset, self).save(*args, **kwargs)
    
    def get_asset_type(self):
        return self.asset_type.name
    
    def status(self):
        if self.assetdelegation_set.filter(return_date__isnull=True).exists():
            return "In Use"
        else:
            return "Available"
        
    def get_current_delegation(self):
        if self.assetdelegation_set.filter(return_date__isnull=True).exists():
            return self.assetdelegation_set.get(return_date__isnull=True)
        else:
            return None
    

class AssetDelegation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey('company.User', on_delete=models.CASCADE)
    check_out_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Asset Delegations"
    
    def __str__(self):
        return self.asset.name + " to " + self.employee.username + " on " + str(self.check_out_date)