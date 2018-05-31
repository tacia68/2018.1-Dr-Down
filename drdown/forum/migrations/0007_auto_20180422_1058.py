# Generated by Django 2.0.3 on 2018-04-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20180419_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date of creation', verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(help_text='Date of update', null=True, verbose_name='Updated at'),
        ),
    ]