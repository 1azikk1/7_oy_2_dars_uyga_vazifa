# Generated by Django 5.1.3 on 2025-01-05 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_alter_course_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': [('test permission', 'test permission')], 'verbose_name': 'talaba ', 'verbose_name_plural': 'Talabalar'},
        ),
    ]
