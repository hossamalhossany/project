# Generated by Django 3.2.11 on 2022-01-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20220119_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
