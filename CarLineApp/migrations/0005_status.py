# Generated by Django 2.2 on 2021-04-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarLineApp', '0004_auto_20210416_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('NEXT_LINE', 'Next_Line'), ('WAITING_LINE1', 'Waiting_Line1'), ('DISMISSED', 'Dismissed'), ('HOLD', 'Hold')], default='WAITING_LINE1', max_length=25)),
            ],
        ),
    ]
