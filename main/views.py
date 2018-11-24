from django.shortcuts import render
from .models import Trial
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import GuestForm
from django.http import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import send_mail

def post_list(request):
    posts = Trial.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Trial, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})


def submit_button(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
    else:
        form = GuestForm(request.GET)
    if form.is_valid():
        print('ok')

    message = generate_mail(form)
    return HttpResponse('Tresc maila: ' + message)


def generate_mail(form):
    text = "Potwierdzam przybycie! " + form.cleaned_data['name'] + " " + form.cleaned_data['surname'] + ". "
    try:
        if form.cleaned_data['overnight']:
            text += "Chcę skorzystać z noclegu. "
        else:
            text += "Nie potrzebuję noclegu. "
    except KeyError:
        text += "Nie potrzebuję noclegu. "

    try:
        if form.cleaned_data['bus']:
            text += "Chcę skorzystać z busa. "
        else:
            text += "Nie potrzebuję transportu."
    except KeyError:
        text += "Nie potrzebuję transportu."

    text += "\nMoje uwagi: \n"
    try:
        if form.cleaned_data['comments']:
            text += form.cleaned_data['comments']
        else:
            text += "Brak uwag."
    except KeyError:
        text += "Brak uwag."

    text += "\nUWAGA. JEST TO WERSJA TESTOWA I TWOJE POTWIERDZENIE NIE JEST JESZCZE WYSYŁANE!"

    return text
