# Generated by Django 4.0.3 on 2022-07-15 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telephone_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
