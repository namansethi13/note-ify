# Generated by Django 4.2.1 on 2023-05-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='bio',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
