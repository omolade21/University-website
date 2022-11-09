from email.policy import default
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth.models import AbstractUser






class CustomUser(AbstractUser):
   
    is_student  = models.BooleanField(default=False)


class StudentProfile(models.Model):
    
    GENDER = (
        ('1', "Male"),
        ('2', "Female"),
    )    

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField('Phone Number', help_text="Your Number will not show to People", max_length=25, null=True, blank=True)
    image = models.ImageField("Applicant Photograph", upload_to='individual')
    means_of_id = models.ImageField("Means of Identification", upload_to='individual')
    gender = models.CharField('Gender', max_length=20, choices=GENDER,  null=True, blank=True)
    age = models.PositiveIntegerField('Age', default=1)
    address = models.CharField("Personal Address", max_length=250, null=True, blank=True) 
    occupation = models.CharField("Occupation", max_length=100, null=True, blank=True)
    employer = models.CharField("Employer", max_length=100, null=True, blank=True)
    employer_address = models.CharField("Address of Employer", max_length=250, null=True, blank=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.user.username


    def get_absolute_url(self):
        try:
            return reverse('web:student-profile', kwargs={'username': self.user.username})
        except:
            None

