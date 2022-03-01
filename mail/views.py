from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.conf import settings
from .forms import ContactForm

from django.core.mail import send_mail, BadHeaderError

class contact(View):
  def get(self,request) :
    form =ContactForm()
    return render(request,'mail/home.html', {'form':form})
  

  def post(self,request):
    form =ContactForm(request.POST)
    if form.is_valid():
     name = form.cleaned_data['name']
     myemail = form.cleaned_data['email']
     try:
                send_mail("thanks",name,settings.EMAIL_HOST_USER,[myemail])
     except BadHeaderError:
                return HttpResponse('Invalid header found.')
 
  
    return HttpResponse('thanks')  
