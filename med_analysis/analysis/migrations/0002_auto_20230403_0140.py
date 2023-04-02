from django.db import migrations
from django.utils.text import slugify

def set_slugs(apps, schema_editor):
    Analysis = apps.get_model('analysis', 'Analysis')
    for analysis in Analysis.objects.all():
        analysis.slug = slugify(analysis.name)
        analysis.save()

class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(set_slugs),
    ]