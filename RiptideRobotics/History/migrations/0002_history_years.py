# Generated by Django 4.0.3 on 2022-03-21 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('History', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='years',
            field=models.TextField(default=2022),
            preserve_default=False,
        ),
    ]
