# Generated by Django 2.2 on 2021-07-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobSearch_app', '0006_job_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary_max',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
