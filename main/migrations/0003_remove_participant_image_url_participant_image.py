# Generated by Django 4.2.2 on 2023-06-24 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_total_score_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='image_url',
        ),
        migrations.AddField(
            model_name='participant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='participant_images/'),
        ),
    ]
