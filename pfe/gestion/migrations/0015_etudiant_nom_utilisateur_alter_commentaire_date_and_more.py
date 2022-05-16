# Generated by Django 4.0.4 on 2022-05-16 13:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0014_remove_etudiant_nom_utilisateur_note_etudiant_note_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='nom_utilisateur',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 16, 13, 34, 7, 251154, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='heure',
            field=models.TimeField(default=datetime.datetime(2022, 5, 16, 13, 34, 7, 251154, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 16, 13, 34, 7, 251154, tzinfo=utc), editable=False),
        ),
    ]
