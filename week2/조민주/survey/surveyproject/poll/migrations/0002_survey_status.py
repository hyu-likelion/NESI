# Generated by Django 3.2 on 2021-05-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='status',
            field=models.TextField(default='y', max_length=1),
        ),
    ]
