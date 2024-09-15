# home/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser, PermissionsMixin, BaseModel):
    # Additional fields for the custom user
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

class Role(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class UserRoleMapping(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self):
        return f"{self.user.username} - {self.role.name}"
    
    
class JobRequiredForm(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=255)
    job_address = models.TextField(null=True, blank=True)
    job_role = models.CharField(max_length=255)
    salary_range = models.CharField( max_length=255,null=True, blank=True)