from django.core.mail import EmailMessage
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
# from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 
from .tasks import *
# from celery import task

@shared_task
def SendEmail():
  subject = 'This_Food_Detail_Offer_Type_Post'
  message = f'Hi,thank you for registering in.'
  email_from = settings.EMAIL_HOST_USER
  recipient_list = ["sshrikant919@gmail.com"]
  print("Running my_task at scheduled time!")
  send_mail( subject, message, email_from, recipient_list,)
  print('skdfsfnk')
  # return HttpResponse('send_mail')
print("calling")