# Generated by Django 4.2.5 on 2023-10-11 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_scope_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Статья-раздел', 'verbose_name_plural': 'Связь статья-раздел'},
        ),
    ]
