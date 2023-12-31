# Generated by Django 4.1.7 on 2023-05-23 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_niveauspecialite_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialite1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=150, unique=True, verbose_name='libelle')),
                ('Filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.filiere', verbose_name='Filiere')),
            ],
            options={
                'verbose_name_plural': 'Specialité',
            },
        ),
    ]
