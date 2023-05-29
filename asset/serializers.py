from rest_framework import serializers
from .models import AssetType, Asset, AssetDelegation
class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = '__all__'


class AssetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'name', 'asset_type', 'status', 'get_current_delegation']


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class AssetDelegationSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', read_only=True)
    employee = serializers.CharField(source='get_employee', read_only=True)
    class Meta:
        model = AssetDelegation
        fields = '__all__'
