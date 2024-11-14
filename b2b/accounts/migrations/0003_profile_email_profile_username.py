# Generated by Django 5.1.3 on 2024-11-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_followers_profile_stanning_profile_stans_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=123, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=11, max_length=20),
            preserve_default=False,
        ),
    ]
