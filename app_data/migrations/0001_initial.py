# Generated by Django 4.0.6 on 2022-08-13 13:12

import app_data.filechecker
import app_data.models
from django.db import migrations, models
import exiffield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', app_data.filechecker.ContentTypeRestrictedFileField(upload_to=app_data.models.user_directory_path)),
                ('file_name', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('file_type', models.CharField(blank=True, editable=False, max_length=15, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('exif', exiffield.fields.ExifField(default={}, editable=False)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
