# Generated by Django 4.1.7 on 2023-08-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_stat_inst', '0015_alter_sievents_form_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sievents',
            name='form_id',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
