# Generated by Django 3.2.11 on 2022-01-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('phone', 'phone'), ('computer', 'computer')], max_length=50, null=True, verbose_name='cat.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, verbose_name='act'),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='please enter name', max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
