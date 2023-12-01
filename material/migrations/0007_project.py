# Generated by Django 4.2.7 on 2023-12-01 11:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0006_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]