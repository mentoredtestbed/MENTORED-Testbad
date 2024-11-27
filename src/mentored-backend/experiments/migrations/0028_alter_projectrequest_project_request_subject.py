# Generated by Django 4.1.4 on 2024-07-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0027_projectrequest_project_request_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrequest',
            name='project_request_subject',
            field=models.CharField(choices=[('Creation', 'Creation'), ('Deactivation', 'Deactivation'), ('Activation', 'Activation')], default='Creation', max_length=20),
        ),
    ]