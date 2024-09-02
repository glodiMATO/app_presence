# Generated by Django 4.1.6 on 2024-08-31 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('numagent', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('postnom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('codedirection', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fonction',
            fields=[
                ('codefonction', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('codegrade', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('numpres', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('datepres', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Prestation',
            fields=[
                ('codeprestation', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('heurearrive', models.TimeField()),
                ('heuredepart', models.TimeField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_presence.agent')),
                ('presence', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_presence.presence')),
            ],
        ),
        migrations.CreateModel(
            name='Carte',
            fields=[
                ('codecarte', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('anneeobtention', models.CharField(max_length=100)),
                ('anneeexpiration', models.CharField(max_length=100)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_presence.agent')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_presence.direction'),
        ),
        migrations.AddField(
            model_name='agent',
            name='fonction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_presence.fonction'),
        ),
        migrations.AddField(
            model_name='agent',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_presence.grade'),
        ),
    ]
