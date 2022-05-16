# Generated by Django 4.0.4 on 2022-05-16 12:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='nom_utilisateur',
            field=models.CharField(default=0, max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='nom_utilisateur',
            field=models.CharField(default=0, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 16, 12, 4, 12, 845571, tzinfo=utc)),
        ),
    ]