# Generated by Django 4.2.7 on 2023-12-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characterforge', '0002_alter_characterclass_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterspell',
            name='level_learned',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
