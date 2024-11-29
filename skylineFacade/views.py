from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from skylineFacade.models import *
from django.views.decorators.csrf import csrf_protect


def home(request):
    services = Services.objects.all()
    blogs = BlogPost.objects.all()
    projects = MajorProjects.objects.all()[:6]
    return render(request,'index.html',{'services':services,'blogs':blogs,'projects':projects})


def aboutus(request):
    return render(request,'aboutus.html')

def projects(request):
    projects = MajorProjects.objects.all()
    return render(request,'projects.html',{'projects':projects})

def projectsDetails(request,slug):
    project = get_object_or_404(MajorProjects, slug=slug)
    return render(request,'project_details.html',{'project':project})

def careers(request):
    return render(request,'careers.html')

def services(request):
    services = Services.objects.all()
    return render(request,'services.html',{'services':services})


def services_details(request,slug):
    service = get_object_or_404(Services, slug=slug)
    return render(request,'services_details.html',{'service':service})


def contact_us(request):
    return render(request,'contactus.html')

def blogs(request):
    blogs = BlogPost.objects.all()
    return render(request,'blogs.html',{'blogs':blogs})


def blogs_details(request,slug):
    blogs = get_object_or_404(BlogPost, slug=slug)
    return render(request,'blog_details.html',{'blogs':blogs})


def Facade_Engineering_Services(request):
    return render(request,'facade-engineering-services.html')


def Facade_Design_Consultancy(request):
    return render(request,'facade-eng-consultancy.html')


def products(request):
    products = Products.objects.get(slug = '1-products')
    
    return render(request,'product.html',context={'product':products})