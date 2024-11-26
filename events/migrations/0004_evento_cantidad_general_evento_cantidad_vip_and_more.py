# Generated by Django 5.1.3 on 2024-11-26 17:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_evento_ciudad_alter_evento_direccion_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='cantidad_general',
            field=models.PositiveIntegerField(default=0, help_text='Cantidad de entradas generales disponibles'),
        ),
        migrations.AddField(
            model_name='evento',
            name='cantidad_vip',
            field=models.PositiveIntegerField(default=0, help_text='Cantidad de entradas VIP disponibles'),
        ),
        migrations.AddField(
            model_name='registracion',
            name='tipo_entrada',
            field=models.CharField(choices=[('general', 'General'), ('vip', 'VIP')], default='general', max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='registracion',
            unique_together={('evento', 'usuario', 'tipo_entrada')},
        ),
    ]