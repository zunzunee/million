# Generated by Django 3.1.5 on 2021-01-17 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('million_songs', '0012_auto_20210117_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='million_songs.units'),
        ),
    ]