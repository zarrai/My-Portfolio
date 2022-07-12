from django.shortcuts import render
from django.http import JsonResponse
from decouple import config
from django.conf import settings
from django.core.mail import send_mail
from .forms import MessageForm
from .models import (
    Competence,
    Education,
    Experience,
    Project,
    Information,
    Message,
)

def email_send(data):
    old_message = Message.objects.last()
    if old_message.name == data['name'] and old_message.email == data['email'] and old_message.message == data['message']:
        return False
    subject = 'Portfolio : Mail from {}'.format(data['name'])
    message = '{}\nSender Email: {}'.format(data['message'], data['email'])
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER, ]
    send_mail(subject, message, email_from, recipient_list)
    return True

def Home(request):
    template_name = 'portfolio/homePage.html'
    context = {}

    if request.method == 'POST':
        if request.POST.get('rechaptcha', None):
            form = MessageForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                data = {
                    'name': request.POST['name'],
                    'email': request.POST['email'],
                    'message': request.POST['message']
                }
                if email_send(data):
                    form.save()

                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        return JsonResponse({'success': False, 'errors': "Oops, you have to check the recaptcha !"})

    if request.method == 'GET':
        form = MessageForm()
        competences = Competence.objects.all().order_by('id')
        education = Education.objects.all().order_by('-id')
        experiences = Experience.objects.all().order_by('-id')
        projects = Project.objects.filter(show_in_slider=True).order_by('-id')
        info = Information.objects.first()
        context = {
            'info': info,
            'competences': competences,
            'education': education,
            'experiences': experiences,
            'projects': projects,
            'form': form,
            'recaptcha_key': config("recaptcha_site_key", default="")
        }
    return render(request, template_name, context)
