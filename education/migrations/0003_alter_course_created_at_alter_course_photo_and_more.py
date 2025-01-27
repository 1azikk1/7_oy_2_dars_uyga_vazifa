# Generated by Django 5.1.3 on 2025-01-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_course_photo_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='course',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/photos', verbose_name='Rasmi'),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti'),
        ),
    ]
