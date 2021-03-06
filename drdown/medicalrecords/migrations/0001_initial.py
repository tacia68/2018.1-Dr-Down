# Generated by Django 2.0.3 on 2018-04-24 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0012_auto_20180423_1542'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(help_text='Patient Care Day', verbose_name='Created at')),
                ('message', models.TextField(help_text='Message of post', max_length=4000, verbose_name='Message')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name': 'Medical Record',
                'verbose_name_plural': 'Medical Records',
            },
        ),
    ]
