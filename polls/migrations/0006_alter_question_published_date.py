# Generated by Django 4.0.2 on 2022-05-19 21:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_question_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
    ]
