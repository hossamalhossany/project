# Generated by Django 3.2.11 on 2022-01-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_login_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
