from django.contrib import admin
from .models import Job,Resume, Technology
# Register your models here.

admin.site.register(Job)
admin.site.register(Technology)
admin.site.register(Resume)
