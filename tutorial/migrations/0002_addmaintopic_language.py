# Generated by Django 3.1 on 2020-09-03 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmaintopic',
            name='language',
            field=models.CharField(default=True, max_length=10000),
        ),
    ]
