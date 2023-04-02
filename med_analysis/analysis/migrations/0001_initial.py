# Generated by Django 4.1.7 on 2023-04-02 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AnalysisResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('date', models.DateField()),
                ('lower_limit', models.FloatField()),
                ('upper_limit', models.FloatField()),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.analysis')),
            ],
        ),
        migrations.AddField(
            model_name='analysis',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.lab'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='measurement_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.measurementunit'),
        ),
    ]