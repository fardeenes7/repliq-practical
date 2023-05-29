from django.shortcuts import render
from rest_framework import viewsets
from company.models import Company, Role, User
from api.serializers import CompanySerializer, RoleSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # The below line is for token authentication
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CompanySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CompanySerializer(instance)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CompanySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get_queryset(self):
        return Company.objects.all()




class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    # The below line is for token authentication
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RoleSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = RoleSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RoleSerializer(instance)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RoleSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get_queryset(self):
        return Role.objects.all()
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # The below line is for token authentication
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get_queryset(self):
        return User.objects.all()
    