# Generated by Django 2.0.1 on 2018-06-28 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_name', models.CharField(error_messages={'unique': 'risk_name must be unique'}, max_length=100, unique=True)),
                ('risk_description', models.CharField(blank=True, default='', max_length=100)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_risks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='riskfield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_field_value', models.CharField(blank=True, default='', max_length=100)),
                ('risk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='risk_riskfields', to='riskapi.risk')),
            ],
        ),
        migrations.CreateModel(
            name='risktype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_type_name', models.CharField(error_messages={'unique': 'risk_type_name must be unique'}, max_length=100, unique=True)),
                ('risk_type_description', models.CharField(blank=True, default='', max_length=100)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_risktypes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='risktypefield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_type_field_name', models.CharField(max_length=100)),
                ('risk_type_field_enum', models.CharField(blank=True, default='', max_length=10)),
                ('risk_type_field_description', models.CharField(blank=True, default='', max_length=100)),
                ('risktype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='risktype_risktypefields', to='riskapi.risktype')),
            ],
        ),
        migrations.AddField(
            model_name='riskfield',
            name='risktypefield',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='riskapi.risktypefield'),
        ),
        migrations.AddField(
            model_name='risk',
            name='risktype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='riskapi.risktype'),
        ),
    ]
