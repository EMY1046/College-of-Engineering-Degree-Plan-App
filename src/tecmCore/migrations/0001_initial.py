# Generated by Django 2.2 on 2019-04-13 02:27

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('tecmCoreInfo', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
