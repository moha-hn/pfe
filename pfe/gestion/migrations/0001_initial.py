# Generated by Django 4.0.4 on 2022-05-15 14:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('specialite', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('groupe', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('specialite', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='section',
            fields=[
                ('nom', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.CharField(max_length=2500)),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, upload_to=None)),
                ('publieur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.enseignant')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.CharField(max_length=250)),
                ('administration', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.administration')),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.enseignant')),
                ('etudiant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.section'),
        ),
        migrations.CreateModel(
            name='commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.CharField(max_length=250)),
                ('enseignant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.enseignant')),
                ('etudiant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.etudiant')),
            ],
        ),
    ]
