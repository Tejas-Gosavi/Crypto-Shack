# Generated by Django 3.2.7 on 2021-09-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(blank=True, default=0)),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(blank=True, default=0)),
                ('price_change_percentage_24h', models.FloatField(blank=True, default=0)),
                ('market_cap', models.FloatField(blank=True, default=0)),
                ('image', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['rank'],
            },
        ),
    ]
