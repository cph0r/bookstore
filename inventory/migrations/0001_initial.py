# Generated by Django 3.2.4 on 2021-06-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookStore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('stock', models.IntegerField(default=0)),
                ('modified_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
