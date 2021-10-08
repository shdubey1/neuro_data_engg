# Generated by Django 3.1.4 on 2021-10-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nde', '0006_auto_20210924_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='EDAJSON',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missing_vals', models.CharField(max_length=10000)),
                ('correlation', models.CharField(max_length=10000)),
                ('missing_vals_plotting', models.CharField(max_length=10000)),
                ('sample_of_first_n_last_rows', models.CharField(max_length=10000)),
                ('graphs', models.CharField(max_length=10000)),
            ],
        ),
    ]
