# Generated by Django 4.2.16 on 2024-11-01 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControleLab', '0013_alter_relatorio_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatorio',
            name='data',
            field=models.CharField(default=datetime.date(2024, 11, 1), max_length=12),
        ),
    ]
