# Generated by Django 4.2.11 on 2024-05-24 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ican', '0015_rename_photocopy_businessdata_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessdata',
            name='reg_number',
            field=models.CharField(blank=True, max_length=21),
        ),
    ]
