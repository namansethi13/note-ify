# Generated by Django 4.2.1 on 2023-05-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userdetails_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
