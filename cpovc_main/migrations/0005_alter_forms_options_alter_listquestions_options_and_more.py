# Generated by Django 4.1.7 on 2023-08-14 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0004_alter_forms_date_ended_alter_forms_form_area_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forms',
            options={'verbose_name': 'Generic Form', 'verbose_name_plural': 'Generic Forms'},
        ),
        migrations.AlterModelOptions(
            name='listquestions',
            options={'verbose_name': 'Generic Question', 'verbose_name_plural': 'Generic Questions'},
        ),
        migrations.AddField(
            model_name='listquestions',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpovc_main.forms'),
        ),
    ]
