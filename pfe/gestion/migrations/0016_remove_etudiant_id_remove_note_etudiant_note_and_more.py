# Generated by Django 4.0.4 on 2022-05-16 13:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0015_etudiant_nom_utilisateur_alter_commentaire_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='id',
        ),
        migrations.RemoveField(
            model_name='note',
            name='etudiant_note',
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 16, 13, 58, 12, 81462, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='heure',
            field=models.TimeField(default=datetime.datetime(2022, 5, 16, 13, 58, 12, 81462, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='nom_utilisateur',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 16, 13, 58, 12, 65685, tzinfo=utc), editable=False),
        ),
    ]