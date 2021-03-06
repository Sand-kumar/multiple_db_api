# Generated by Django 4.0.4 on 2022-05-11 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voters',
            fields=[
                ('ac_no', models.SmallIntegerField()),
                ('part_no', models.SmallIntegerField()),
                ('section_no', models.SmallIntegerField()),
                ('serial_no', models.SmallIntegerField()),
                ('houseno', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('relname', models.TextField(blank=True, null=True)),
                ('rtype', models.TextField(blank=True, null=True)),
                ('epic_no', models.TextField(blank=True, null=True)),
                ('contactno', models.TextField(blank=True, null=True)),
                ('pincode', models.FloatField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'voters',
                'managed': False,
            },
        ),
    ]
