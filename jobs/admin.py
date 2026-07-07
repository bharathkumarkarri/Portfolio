from django.contrib import admin
from .models import Profile, Technology, Job, ProjectImage, Skill, Experience, Education, Certificate, Resume

# Inline for Project Gallery Screenshots
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'published_date', 'is_featured')
    search_fields = ('title', 'summary', 'short_description')
    list_filter = ('status', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location', 'availability')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class', 'order')
    list_editable = ('order',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date', 'order')
    list_editable = ('order',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'duration', 'cgpa', 'order')
    list_editable = ('order',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'year', 'order')
    list_editable = ('order',)

admin.site.register(Technology)
admin.site.register(Resume)
