# Generated by Django 5.2 on 2025-04-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_conteoproduccion_options_alter_maquina_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquina',
            name='tipo',
            field=models.CharField(choices=[('Empaquetadora', 'Empaquetadora'), ('Cubrebocas', 'Cubrebocas')], max_length=50),
        ),
    ]
