# Generated by Django 4.1.4 on 2024-07-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0024_alter_projectrequest_project_admin_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrequest',
            name='project_admin_response',
            field=models.TextField(null=True),
        ),
    ]