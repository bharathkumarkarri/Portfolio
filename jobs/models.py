from django.db import models
import os
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.

class Profile(models.Model):
    greeting = models.CharField(max_length=100, default="Hello, I'm")
    name = models.CharField(max_length=100)
    titles = models.CharField(max_length=255, help_text="Comma-separated list of professions for typing effect, e.g. Full Stack Developer, Python Developer")
    tagline = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    
    email = models.EmailField()
    location = models.CharField(max_length=100, default="Vizag")
    availability = models.CharField(max_length=100, default="Freelance / Full-time")
    
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    profile_photo = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Job(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, max_length=250)
    tech = models.ManyToManyField(Technology)
    summary = models.TextField(max_length=1000)
    
    short_description = models.CharField(max_length=255, blank=True)
    overview = models.TextField(blank=True)
    features = models.TextField(blank=True, help_text="Enter key features (HTML/plain text is supported)")
    challenges = models.TextField(blank=True, help_text="Enter challenges and solutions")
    status = models.CharField(max_length=50, default="Completed")
    published_date = models.CharField(max_length=50, blank=True, help_text="e.g. July 2026")
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    link = models.URLField(blank=True)
    gitlink = models.URLField(blank=True)

    @property
    def features_list(self):
        return self._parse_points(self.features, split_on_comma=True)

    @property
    def challenges_list(self):
        return self._parse_points(self.challenges, split_on_comma=False)

    def _parse_points(self, text, split_on_comma=False):
        if not text:
            return []
        import re
        
        # Helper to strip HTML tags
        def strip_tags(html):
            cleaned = re.sub(r'<[^>]+>', '', html)
            return cleaned.strip()

        # Check if it contains HTML
        if bool(re.search(r'<[^>]+>', text)):
            # It has HTML. Let's try to extract heading-paragraph pairs:
            pairs = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>\s*<p[^>]*>(.*?)</p>', text, re.DOTALL | re.IGNORECASE)
            if pairs:
                return [f"<strong>{strip_tags(h)}</strong>: {strip_tags(p)}" for h, p in pairs]
            
            # If it contains HTML but not heading-paragraph pairs, let's see if there are list items:
            lis = re.findall(r'<li[^>]*>(.*?)</li>', text, re.DOTALL | re.IGNORECASE)
            if lis:
                return [strip_tags(li) for li in lis]
                
            # If it's just paragraphs, treat each paragraph as an item:
            ps = re.findall(r'<p[^>]*>(.*?)</p>', text, re.DOTALL | re.IGNORECASE)
            if ps:
                return [strip_tags(p) for p in ps]
            
            # Fallback if other HTML
            return [strip_tags(text)]

        # Split by newlines first
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        if len(lines) > 1:
            raw_items = lines
        elif split_on_comma:
            # Split by commas
            raw_items = [item.strip() for item in text.split(',') if item.strip()]
        else:
            raw_items = [text.strip()]
            
        cleaned_items = []
        for item in raw_items:
            # Strip leading bullet/list symbols
            cleaned = re.sub(r'^(?:[•\-\*\+\u2022\u2023\u25E6\u2043\u204F]|\d+[\.\-\)]\s*)\s*', '', item).strip()
            if cleaned:
                cleaned_items.append(cleaned)
        return cleaned_items

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Job.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Job, related_name="gallery_images", on_delete=models.CASCADE)
    image = CloudinaryField('image')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Gallery image for {self.project.title}"


class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=100, blank=True, help_text="FontAwesome icon class, e.g. fa-brands fa-nodejs (leave blank to auto-assign)")
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.icon_class or self.icon_class.strip() == "":
            name_lower = self.name.lower().strip()
            
            # Map common skill keywords to FontAwesome classes
            mapping = {
                "python": "fa-brands fa-python",
                "django": "fa-solid fa-server",
                "react": "fa-brands fa-react",
                "javascript": "fa-brands fa-js",
                "js": "fa-brands fa-js",
                "typescript": "fa-brands fa-js",
                "ts": "fa-brands fa-js",
                "html": "fa-brands fa-html5",
                "css": "fa-brands fa-css3-alt",
                "bootstrap": "fa-brands fa-bootstrap",
                "tailwind": "fa-solid fa-wind",
                "node": "fa-brands fa-node-js",
                "express": "fa-brands fa-node-js",
                "git": "fa-brands fa-git-alt",
                "github": "fa-brands fa-github",
                "docker": "fa-brands fa-docker",
                "aws": "fa-brands fa-aws",
                "amazon": "fa-brands fa-aws",
                "sql": "fa-solid fa-database",
                "mysql": "fa-solid fa-database",
                "postgres": "fa-solid fa-database",
                "postgresql": "fa-solid fa-database",
                "sqlite": "fa-solid fa-database",
                "mongodb": "fa-solid fa-database",
                "mongo": "fa-solid fa-database",
                "c++": "fa-solid fa-code",
                "cpp": "fa-solid fa-code",
                "c#": "fa-solid fa-code",
                "java": "fa-brands fa-java",
                "php": "fa-brands fa-php",
                "laravel": "fa-brands fa-laravel",
                "angular": "fa-brands fa-angular",
                "vue": "fa-brands fa-vuejs",
                "sass": "fa-brands fa-sass",
                "npm": "fa-brands fa-npm",
                "figma": "fa-brands fa-figma",
                "machine learning": "fa-solid fa-brain",
                "ai": "fa-solid fa-brain",
                "artificial intelligence": "fa-solid fa-brain",
                "deep learning": "fa-solid fa-brain",
                "api": "fa-solid fa-gears",
                "rest": "fa-solid fa-gears",
                "linux": "fa-brands fa-linux",
                "window": "fa-brands fa-windows",
                "mac": "fa-brands fa-apple",
            }
            
            matched = False
            for key, val in mapping.items():
                if key in name_lower:
                    self.icon_class = val
                    matched = True
                    break
            
            if not matched:
                self.icon_class = "fa-solid fa-code" # Default code tag fallback
                
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, default="Present")
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    duration = models.CharField(max_length=50, help_text="e.g. 2024 - 2027")
    cgpa = models.CharField(max_length=20, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    verification_link = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


def get_resume_storage():
    from cloudinary_storage.storage import RawMediaCloudinaryStorage
    return RawMediaCloudinaryStorage()


class Resume(models.Model):
    file = models.FileField(upload_to='resumes/', storage=get_resume_storage)
    uploaded_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Get the existing resume (if any)
        old_resume = Resume.objects.exclude(pk=self.pk).first()

        if old_resume:
            # Delete the old file from storage (Cloudinary or local)
            if old_resume.file:
                old_resume.file.delete(save=False)

            # Delete the old database record
            old_resume.delete()

        super().save(*args, **kwargs)

    def __str__(self):
        return "Resume"