# Generated by Django 4.0.3 on 2022-07-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='foods',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='foods',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='foods',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterIndexTogether(
            name='foods',
            index_together={('id',)},
        ),
    ]