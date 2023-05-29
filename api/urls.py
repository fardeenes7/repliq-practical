from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from company.views import CompanyViewSet, RoleViewSet, UserViewSet
from asset.views import AssetTypeViewSet, AssetViewSet, AssetDelegationViewSet

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('company/', CompanyViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('company/<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),

    path('role/',RoleViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('role/<int:pk>/', RoleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),

    path('user/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),

    path('asset_type/', AssetTypeViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('asset_type/<int:pk>/', AssetTypeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),

    path('asset/', AssetViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('asset/<int:pk>/', AssetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('asset/<int:pk>/delegations/', AssetViewSet.as_view({'get': 'get_delegation'})),

    path('asset_delegation/', AssetDelegationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('asset_delegation/<int:pk>/', AssetDelegationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),


]