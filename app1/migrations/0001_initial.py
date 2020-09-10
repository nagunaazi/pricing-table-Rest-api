# Generated by Django 2.0 on 2020-09-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PricingTable',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Plan_Name', models.CharField(max_length=30)),
                ('Plan_Formula', models.CharField(max_length=30)),
                ('Location', models.CharField(max_length=30)),
                ('Plan_Status', models.CharField(max_length=30)),
                ('Created_Date', models.DateField()),
                ('Updated_Date', models.DateField()),
            ],
        ),
    ]
