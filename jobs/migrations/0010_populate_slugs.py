from django.db import migrations

def populate_slugs(apps, schema_editor):
    from django.utils.text import slugify
    Job = apps.get_model('jobs', 'Job')
    for job in Job.objects.all():
        if not job.slug:
            base_slug = slugify(job.title)
            slug = base_slug
            counter = 1
            while Job.objects.filter(slug=slug).exclude(pk=job.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            job.slug = slug
            job.save()

class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_alter_resume_file'),
    ]

    operations = [
        migrations.RunPython(populate_slugs),
    ]
