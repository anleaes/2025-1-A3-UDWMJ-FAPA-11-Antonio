# Generated by Django 5.2 on 2025-06-13 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria')),
            ],
        ),
    ]
