# Generated by Django 4.1.7 on 2023-04-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_users', '0004_alter_event_card_id_alter_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='card_id',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='labuser',
            name='card_id',
            field=models.CharField(max_length=8),
        ),
    ]
