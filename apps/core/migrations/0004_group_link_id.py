# Generated by Django 4.2.6 on 2023-10-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='link_id',
            field=models.CharField(max_length=6, null=True, verbose_name='Link Id'),
        ),
    ]