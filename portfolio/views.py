from django.shortcuts import render
from . models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def home(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'index.html', context)

def single_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project' : project
    }
    return render(request, 'single-project.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        obj = request.POST.get("object", "")
        message = request.POST.get("message", "")
        email = request.POST.get("email", "")
        email_context = {
            "name" : name,
            "obj" : obj,
            "message" : message,
            "email" : email
        }

        template_email = render_to_string('email_template.html', email_context)
        email_obj = EmailMessage(
            name + " has sent an email",
            template_email,
            settings.EMAIL_HOST_USER,
            ['strawberry7836@gmail.com']
        )
        email_obj.fail_silently = False
        email_obj.send()
        
    return render(request, "contact.html")

def services(request):
    render(request, "services.html")

def about(request):
    render(request, "about.html")

def portfolio(request):
    categories = Category.objects.all()
    projects = Project.objects.all()
    context = {
        'categories': categories,
        'projects': projects
    }
    return render(request, "portfolio.html", context)