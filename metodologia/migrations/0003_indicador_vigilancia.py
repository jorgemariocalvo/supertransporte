# Generated by Django 3.1.3 on 2020-11-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metodologia', '0002_auto_20201118_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='vigilancia',
            field=models.CharField(choices=[('objetivo', 'objetivo'), ('subjetivo', 'subjetivo')], default='objetivo', max_length=9),
        ),
    ]
