# Generated by Django 3.0.7 on 2021-01-13 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cam_url', models.URLField(max_length=100)),
                ('cam_model', models.CharField(max_length=100)),
                ('stream_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100)),
                ('created_at', models.DateField()),
                ('cam_name', models.CharField(max_length=200)),
                ('cam_user', models.CharField(max_length=200)),
                ('cam_group', models.CharField(choices=[('Cenamatic', 'Cenamatic'), ('Action', 'Action'), ('Macro', 'Macro'), ('Drone', 'Drone'), ('PointToShoot', 'Point To Shoot'), ('Personal', 'Personal')], default='Cenamatic', max_length=200)),
            ],
        ),
    ]