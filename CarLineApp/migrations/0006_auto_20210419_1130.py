# Generated by Django 2.2 on 2021-04-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarLineApp', '0005_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='rider',
            name='status',
            field=models.CharField(default='waiting', max_length=25),
            preserve_default=False,
        ),
    ]
