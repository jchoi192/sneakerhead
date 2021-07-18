# Generated by Django 3.2.4 on 2021-07-17 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_sneakerhead_sneaker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('area', models.CharField(choices=[('IS', 'Inner Sole'), ('MS', 'Mid Sole'), ('OS', 'Outer Sole'), ('L', 'Laces'), ('T', 'Tongue')], default='IS', max_length=2)),
                ('sneaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.sneaker')),
            ],
        ),
    ]