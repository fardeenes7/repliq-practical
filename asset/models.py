from django.db import models
from django.utils import timezone

# Create your models here.

class AssetType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Asset Types"
    
    def __str__(self):
        return self.name
    

class Asset(models.Model):
    CONDITION_CHOICES = (
        ('New', 'New'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
        ('Broken', 'Broken'),
    )
    name = models.CharField(max_length=50)
    asset_type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='New')
    purchase_date = models.DateField(default=timezone.now)
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
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
        
    def is_available(self):
        if self.assetdelegation_set.filter(return_date__isnull=True).exists():
            return False
        else:
            return True
        
    def get_current_delegation(self):
        if self.assetdelegation_set.filter(return_date__isnull=True).exists():
            return self.assetdelegation_set.get(return_date__isnull=True)
        else:
            return None
    

class AssetDelegation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey('company.User', on_delete=models.CASCADE)
    delegated_by = models.ForeignKey('company.User', related_name='delegated_by', on_delete=models.SET_NULL, null=True, blank=True)
    check_out_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Asset Delegations"

    def get_status_display(self):
        if self.return_date:
            return "Returned"
        else:
            return "In Use"
        
    def get_employee(self):
        return self.employee.get_full_name()
    
    def __str__(self):
        return self.asset.name + " to " + self.employee.username + " on " + str(self.check_out_date)