# Generated by Django 3.2.13 on 2022-05-01 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0003_auto_20220501_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
