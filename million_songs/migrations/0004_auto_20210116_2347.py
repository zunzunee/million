# Generated by Django 3.1.5 on 2021-01-16 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('million_songs', '0003_auto_20210116_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='cd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='million_songs.cds'),
        ),
    ]