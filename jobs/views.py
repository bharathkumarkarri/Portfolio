from django.shortcuts import render, get_object_or_404
from .models import Profile, Technology, Job, Skill, Experience, Education, Certificate, Resume

# Helper fallback profile when database doesn't have a profile yet
def get_fallback_profile():
    return {
        "greeting": "Hi, I'm",
        "name": "Karri Bharath Kumar",
        "titles": "Full Stack Developer, Python Developer, Django Expert",
        "tagline": "Computer Science undergraduate passionate about AI-powered software engineering, backend systems, and building scalable, intelligent web applications.",
        "bio": "I am an aspiring Software Engineer passionate about building practical and impactful applications. Currently, I am expanding my knowledge in backend development, databases, and modern web technologies while preparing for opportunities in software engineering.",
        "email": "bharath.karri23@gmail.com",
        "location": "Vizag",
        "availability": "Freelance / Full-time",
        "github_link": "https://github.com/bharathkumarkarri",
        "linkedin_link": "https://www.linkedin.com/in/bharath-kumar-karri/"
    }

def homepage(request):
    profile = Profile.objects.first()
    if not profile:
        profile = get_fallback_profile()
        
    resumes = Resume.objects.first()
    jobs = Job.objects.filter(is_featured=True).order_by('-id')
    skills = Skill.objects.all().order_by('order')
    experiences = Experience.objects.all().order_by('order')
    educations = Education.objects.all().order_by('order')
    certificates = Certificate.objects.all().order_by('order')
    
    context = {
        'profile': profile,
        'resumes': resumes,
        'jobs': jobs,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'certificates': certificates,
    }
    return render(request, 'jobs/home.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Job, slug=slug)
    profile = Profile.objects.first()
    if not profile:
        profile = get_fallback_profile()
        
    resumes = Resume.objects.first()
    gallery_images = project.gallery_images.all()
    
    # Calculate Prev / Next projects
    all_projects = list(Job.objects.all().order_by('id'))
    prev_project = None
    next_project = None
    try:
        idx = all_projects.index(project)
        if idx > 0:
            prev_project = all_projects[idx - 1]
        if idx < len(all_projects) - 1:
            next_project = all_projects[idx + 1]
    except ValueError:
        pass

    # Find related projects (sharing at least one tech stack badge)
    project_tech_ids = project.tech.values_list('id', flat=True)
    related_projects = Job.objects.filter(tech__id__in=project_tech_ids).exclude(id=project.id).distinct()[:3]

    context = {
        'project': project,
        'profile': profile,
        'resumes': resumes,
        'gallery_images': gallery_images,
        'prev_project': prev_project,
        'next_project': next_project,
        'related_projects': related_projects,
    }
    return render(request, 'jobs/project.html', context)


def projects_list(request):
    profile = Profile.objects.first()
    if not profile:
        profile = get_fallback_profile()
        
    resumes = Resume.objects.first()
    jobs = Job.objects.all().order_by('-id')
    technologies = Technology.objects.all()

    context = {
        'profile': profile,
        'resumes': resumes,
        'jobs': jobs,
        'technologies': technologies,
    }
    return render(request, 'jobs/projects_list.html', context)


def certificates_list(request):
    profile = Profile.objects.first()
    if not profile:
        profile = get_fallback_profile()
        
    resumes = Resume.objects.first()
    certificates = Certificate.objects.all().order_by('order')

    context = {
        'profile': profile,
        'resumes': resumes,
        'certificates': certificates,
    }
    return render(request, 'jobs/certificates_list.html', context)