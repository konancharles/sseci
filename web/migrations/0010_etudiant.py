# Generated by Django 4.1.7 on 2023-05-22 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_alter_commune_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('prenom', models.CharField(max_length=20, verbose_name='Prenom')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('contact', models.CharField(max_length=50, unique=True, verbose_name='Contact')),
                ('matricule', models.CharField(max_length=50, unique=True, verbose_name='Matricule')),
                ('lieu_de_naissance', models.DateField(max_length=20, verbose_name='Lieu de Naissance')),
                ('date_de_naissance', models.CharField(max_length=20, verbose_name='Date de Naissance')),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.commune', verbose_name='Commune')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.filiere', verbose_name='Filière')),
                ('niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.niveau', verbose_name='Niveau')),
                ('sexe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.sexe', verbose_name='Sexe')),
                ('specialite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.specialite', verbose_name='Specialité')),
                ('ufr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ufr', verbose_name='Ufr')),
                ('universite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.universite', verbose_name='Université')),
                ('ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ville', verbose_name='Ville')),
            ],
            options={
                'verbose_name_plural': 'Etudiant',
            },
        ),
    ]
