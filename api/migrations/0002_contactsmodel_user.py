# Generated by Django 3.0 on 2020-09-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactsmodel',
            name='user',
            field=models.CharField(blank='True', max_length=100, null=True),
        ),
    ]
