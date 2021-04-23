# Generated by Django 2.2 on 2021-04-19 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarLineApp', '0006_auto_20210419_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='rider',
            name='carline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='riders', to='CarLineApp.Carline'),
        ),
    ]
