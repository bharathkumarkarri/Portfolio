from django.db import models
import os
from cloudinary.models import CloudinaryField

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Job(models.Model):
    # image = models.ImageField(upload_to='images/')
    image = CloudinaryField('image')
    title = models.CharField(max_length=200)
    tech = models.ManyToManyField(Technology)
    summary = models.TextField(max_length=1000)
    link = models.URLField(blank=True)
    gitlink = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Get the existing resume (if any)
        old_resume = Resume.objects.exclude(pk=self.pk).first()

        if old_resume:
            # Delete the old file from disk
            if old_resume.file and os.path.isfile(old_resume.file.path):
                os.remove(old_resume.file.path)

            # Delete the old database record
            old_resume.delete()

        super().save(*args, **kwargs)

    def __str__(self):
        return "Resume"