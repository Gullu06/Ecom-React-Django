# Generated by Django 4.2.2 on 2023-12-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('annual_income', models.IntegerField()),
                ('investment', models.IntegerField()),
            ],
        ),
    ]
