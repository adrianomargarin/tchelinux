# Generated by Django 2.1 on 2018-08-18 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('start_date', models.DateTimeField(verbose_name='Data de início')),
                ('end_date', models.DateTimeField(verbose_name='Data de fim')),
                ('location', models.CharField(max_length=255, verbose_name='Local')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
    ]
