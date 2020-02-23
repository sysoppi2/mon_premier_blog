# Generated by Django 2.0.13 on 2020-02-17 11:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('arriere_boutique', '0009_auto_20200216_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='nom_categorie',
            new_name='titre',
        ),
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]