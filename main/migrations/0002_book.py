# Generated by Django 5.0.6 on 2024-05-27 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('img', models.ImageField(upload_to='')),
                ('avtors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.avtor')),
            ],
        ),
    ]