# Generated by Django 5.1.3 on 2025-01-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_alter_course_created_at_alter_course_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Rasmi'),
        ),
    ]
