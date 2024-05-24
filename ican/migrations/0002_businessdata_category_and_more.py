# Generated by Django 4.2.11 on 2024-05-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ican', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessdata',
            name='category',
            field=models.CharField(default='retail', max_length=50),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='email_id',
            field=models.EmailField(max_length=60),
        ),
    ]
