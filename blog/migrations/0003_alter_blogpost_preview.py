# Generated by Django 5.1.1 on 2024-09-23 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_options_remove_blogpost_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='blog_previews/', verbose_name='Превью'),
        ),
    ]