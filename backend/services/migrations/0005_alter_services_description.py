# Generated by Django 4.0.4 on 2022-05-07 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_services_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]