# Generated by Django 4.2.16 on 2024-09-25 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ControleLab', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computador',
            old_name='staus',
            new_name='status',
        ),
    ]
