# Generated by Django 3.2.4 on 2021-07-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_cleaning'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cleaning',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='date',
            field=models.DateField(verbose_name='Cleaned on: '),
        ),
    ]