from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.


def home(request):
    return render(request, 'send_email_project/home.html')


def email_sent(request):
    return render(request, 'send_email_project/email_sent.html')


def index(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('emailat')
        message_html = render_to_string('send_email_project/message.html')
        plain_message = strip_tags(message_html)
        email_split = email.split(sep=' ')
        for i in email_split:
            send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [i], fail_silently=False)
            if not i:
                break
        return redirect('/email_sent')
    return render(request, 'send_email_project/send_email.html')
