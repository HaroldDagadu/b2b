# Generated by Django 5.1.3 on 2024-11-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
