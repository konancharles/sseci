# Generated by Django 4.1.7 on 2023-10-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_etudiant_carte_cni_etudiant_carte_etudiant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='carte_etudiant',
            field=models.FileField(blank=True, max_length=150, null=True, upload_to='CarteEtudiant', verbose_name="Carte d'etudiant"),
        ),
    ]
