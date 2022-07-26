from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView

from my_portfolio.blog.models import Post

from .forms import MessageForm
from .models import Competence, Education, Experience, Information, Project


def email_send(data):
    # old_message = Message.objects.last()
    # if old_message.name == data['name'] and old_message.email == data['email'] and old_message.message == data['message']: # noqa: E501
    #     return False
    subject = "Portfolio : Mail from {}".format(data["name"])
    message = "{}\nSender Email: {}".format(data["message"], data["email"])
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [
        settings.EMAIL_HOST_USER,
    ]
    send_mail(subject, message, email_from, recipient_list)
    return True


def Home(request):
    template_name = "portfolio/homePage.html"
    context = {}

    if request.method == "POST":
        if request.POST.get("rechaptcha", None):
            form = MessageForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                data = {
                    "name": request.POST["name"],
                    "email": request.POST["email"],
                    "message": request.POST["message"],
                }
                if email_send(data):
                    form.save()

                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "errors": form.errors})
        return JsonResponse(
            {"success": False, "errors": "Oops, you have to check the recaptcha !"}
        )

    if request.method == "GET":
        form = MessageForm()
        competences = Competence.objects.all().order_by("id")
        education = Education.objects.all().order_by("-the_year")
        experiences = Experience.objects.all().order_by("-the_year")
        projects = Project.objects.filter(show_in_slider=True).order_by("-id")
        info = Information.objects.first()
        posts = Post.objects.filter(featured=True).order_by("-id")
        context = {
            "info": info,
            "competences": competences,
            "education": education,
            "experiences": experiences,
            "projects": projects,
            "form": form,
            "posts": posts,
            "recaptcha_key": "",
            "keywords": settings.META_DEFAULT_KEYWORDS,
        }
    return render(request, template_name, context)


def projectsPage(request):
    template_name = "portfolio/projects/projects_page.html"
    if request.method == "GET":
        projects = Project.objects.all().order_by("-id")
        context = {"projects": projects}
        return render(request, template_name, context)


def projectDetail(request, slug):
    template_name = "portfolio/projects/project_detail.html"
    if request.method == "GET":
        project = get_object_or_404(Project, slug=slug)
        meta = project.as_meta()
        return render(request, template_name, {"project": project, "meta": meta})


def search(request):
    if request.method == "POST":
        search_text = request.POST.get("searchText", False)
        if search_text:
            lookups = (
                Q(title__icontains=search_text)
                | Q(description__icontains=search_text)
                | Q(tags__name__icontains=search_text)
            )

            objs = Project.objects.filter(lookups)
            if objs:
                projects = Project.objects.filter(lookups).values()
                projects = list(projects)
                for project, obj in zip(projects, objs):
                    project.update(
                        {"url": obj.get_absolute_url(), "image_url": obj.image.url}
                    )
                return JsonResponse(
                    {"success": True, "projects": projects, "searchText": search_text}
                )
    return JsonResponse({"success": False, "searchText": search_text})


def handler404(request, exception):
    return render(request, "404.html", status=404)


class privacypolicy(TemplateView):
    template_name = "privacypolicy.html"
