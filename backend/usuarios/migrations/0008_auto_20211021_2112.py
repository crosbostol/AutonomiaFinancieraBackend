# Generated by Django 3.0.7 on 2021-10-22 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20211020_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='cases_client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='RUT', to='usuarios.Teacher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='cases_teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='RUT', to='usuarios.Client'),
            preserve_default=False,
        ),
    ]
