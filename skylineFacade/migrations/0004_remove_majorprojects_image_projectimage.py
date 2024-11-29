# Generated by Django 4.2.4 on 2024-11-18 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skylineFacade', '0003_majorprojects_facede_materials_majorprojects_scope'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='majorprojects',
            name='image',
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='skylineFacade.majorprojects')),
            ],
        ),
    ]
