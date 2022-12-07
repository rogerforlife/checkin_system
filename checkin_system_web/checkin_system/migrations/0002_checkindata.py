# Generated by Django 2.2.11 on 2022-11-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkindata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=11)),
                ('checkin_date', models.DateField(auto_now_add=True)),
                ('timein', models.DateTimeField(null=True)),
                ('timeout', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['employee_id'],
                'unique_together': {('employee_id', 'checkin_date')},
            },
        ),
    ]
