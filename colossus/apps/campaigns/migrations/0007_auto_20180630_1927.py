# Generated by Django 2.0.6 on 2018-06-30 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0006_auto_20180630_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='total_clicks_count',
            field=models.PositiveIntegerField(default=0, verbose_name='total clicks'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='total_opens_count',
            field=models.PositiveIntegerField(default=0, verbose_name='total opens'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='unique_clicks_count',
            field=models.PositiveIntegerField(default=0, verbose_name='unique clicks'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='unique_opens_count',
            field=models.PositiveIntegerField(default=0, verbose_name='unique opens'),
        ),
    ]