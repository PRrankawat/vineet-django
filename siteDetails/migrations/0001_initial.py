# Generated by Django 3.1.3 on 2021-07-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteDetail',
            fields=[
                ('siteID', models.AutoField(primary_key=True, serialize=False)),
                ('site_name', models.CharField(max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'site_detail',
            },
        ),
    ]
