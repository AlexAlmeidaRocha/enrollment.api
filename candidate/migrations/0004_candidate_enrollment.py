# Generated by Django 4.2 on 2023-04-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0001_initial'),
        ('candidate', '0003_candidate_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='enrollment',
            field=models.ManyToManyField(to='enrollment.enrollment'),
        ),
    ]
