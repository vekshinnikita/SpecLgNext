# Generated by Django 4.0.4 on 2022-05-07 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('completed_work', '0002_remove_work_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='date',
            field=models.CharField(max_length=150, null=True, verbose_name='Месяц и год'),
        ),
    ]
