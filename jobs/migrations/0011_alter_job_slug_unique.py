from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_populate_slugs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
