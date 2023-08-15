# Generated by Django 4.1.7 on 2023-05-21 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_ufr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=150, unique=True, verbose_name='libelle')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Code')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('contact', models.CharField(max_length=20, unique=True, verbose_name='Contact')),
                ('ufr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ufr', verbose_name='Ufr')),
            ],
            options={
                'verbose_name_plural': 'Filiere',
            },
        ),
    ]