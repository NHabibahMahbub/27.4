# Generated by Django 5.0.3 on 2024-04-25 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0015_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='owner_contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
