# Generated by Django 4.2.4 on 2023-10-21 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_alter_clothingrecommendations_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clothingrecommendations',
            options={'verbose_name_plural': 'Clothing recommendations'},
        ),
        migrations.AlterModelOptions(
            name='weatherdata',
            options={'verbose_name_plural': 'Weather Data'},
        ),
    ]
