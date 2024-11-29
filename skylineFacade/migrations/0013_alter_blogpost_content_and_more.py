# Generated by Django 4.2.4 on 2024-11-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skylineFacade', '0012_rename_shor_description_services_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='health_safety',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='majorprojects',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
