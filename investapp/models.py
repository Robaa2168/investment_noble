
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from django.db.models.signals import post_save

def random_string():
    return str(random.randint(10000, 99999))

class UserProfile(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE, blank=True, null=True)
    unique_url = models.CharField(default=random_string, max_length=10)
    phone_number = models.CharField(max_length=14, blank=True)
    account_balance = models.TextField(max_length=6, blank=True)
    invest_balance = models.TextField(max_length=6, blank=True)
    reg_fee = models.TextField(max_length=6, blank=True)
    can_access_features =models.BooleanField(default=False)
    alt_phone_number = models.CharField(max_length=14, blank=True)
    profile_pic_url = models.CharField(max_length=14, blank=True)
    refferer = models.TextField(max_length=20, default='')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            instance.userprofile.save()

            post_save.connect(UserProfile, sender=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        UserProfile.objects.get_or_create(user=instance)
        instance.userprofile.save()


class Investiments(models.Model):
    invoicce = models.TextField(max_length=20)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True)
    amount = models.TextField(max_length=20)
    earnings = models.TextField(max_length=20)
    phone_number = models.TextField(max_length=20)
    invest_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    invest_date = models.DateTimeField(blank=True, null=True)
    period = models.TextField(default='', blank=True)
    percent = models.TextField(default='', blank=True)
    status = models.TextField(default='pending', blank=True)
    control_balance = models.TextField(default='', max_length=20)



class Withdrawals(models.Model):
    WITHDRAWAL_STATUS = (
            ('A', 'Approved'),
            ('P', 'Pending'),
            ('R', 'Rejected'),
        )
    status = models.CharField(max_length=1, choices=WITHDRAWAL_STATUS, default="pending")
    amount = models.TextField(max_length=6, default='' )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True)
    
    
    

