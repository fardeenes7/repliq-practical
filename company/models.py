from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

#Company Class
class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company_logo')
    description = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Companies"
    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Roles"
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.lower()
        super(Role, self).save(*args, **kwargs)
    
class CustomUserManager(models.Manager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_super_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('role', Role.objects.get_or_create(slug='admin')[0])
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **extra_fields)
    
    def get_queryset(self):
        return super().get_queryset().filter(role__slug='employee')

class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    role = models.ForeignKey(Role, related_name='role', on_delete=models.SET_DEFAULT, default=2, null=True, blank=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]
    class Meta:
        verbose_name_plural = "Users"
        swappable = 'AUTH_USER_MODEL'


    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def get_role(self):
        return self.role.name
    
    def get_company(self):
        return self.company.name
    
    def is_admin(self):
        return self.role.name == 'admin'
    
    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

