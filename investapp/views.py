import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from .forms import *
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .models import *
#from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
     investments= Investiments.objects.filter(user=request.user)
     return render(request, template_name='index.html', context={'investments':investments})


def activateaccount(request):
     return render(request, template_name='dashboard.html')


def makeInvestment(request):
     if request.method == "POST":
          period = request.POST.get("period")
          amt = request.POST.get("amount")
          percent_ = 30
          current_date_and_time = datetime.datetime.now()
          future_date_and_time = current_date_and_time
          if period == "24hrs":
               hours_added = datetime.timedelta(hours = 24)
               future_date_and_time = current_date_and_time + hours_added   
               percent_ = 30
          elif period == "4days":
               days_added = datetime.timedelta(days = 4)
               future_date_and_time = current_date_and_time + days_added
               percent_ = 60
          elif period == "7days":
               days_added = datetime.timedelta(days = 7)
               future_date_and_time = current_date_and_time + days_added
               percent_ = 90

          per_ = (100 + percent_) / 100
          earnings =  per_ * int(amt)
          investment=Investiments.objects.create(invoicce="invoice_1", user=request.user, amount=request.POST.get("amount"), control_balance=request.POST.get("amount"), earnings=earnings, phone_number=request.user.userprofile.phone_number, due_date=future_date_and_time, invest_date=current_date_and_time, period=period, percent=percent_)
          i_ = investment.save()
          print(i_)
          if i_ == True:
               return redirect("index")
          else:
               return redirect("index")