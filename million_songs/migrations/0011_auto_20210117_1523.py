# Generated by Django 3.1.5 on 2021-01-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('million_songs', '0010_auto_20210117_1521'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='units',
            name='name_or_song_null',
        ),
        migrations.AddConstraint(
            model_name='units',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('name__isnull', True), ('is_everyone', False)), ('song__isnull', True), _connector='OR'), name='name_or_song_null'),
        ),
    ]