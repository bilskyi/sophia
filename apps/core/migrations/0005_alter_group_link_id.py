# Generated by Django 4.2.6 on 2023-10-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_group_link_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='link_id',
            field=models.CharField(max_length=6, verbose_name='Link Id'),
        ),
    ]
