from zipfile import Path
from django.http import FileResponse
from django.shortcuts import render
from portfolio import settings
from .models import Job,Resume

# Create your views here.
def homepage(request):
    jobs = Job.objects.all()
    resumes = Resume.objects.first()
    return render(request, 'jobs/home.html', {'jobs': jobs, 'resumes': resumes})

def project(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'jobs/project.html', {'job': job})