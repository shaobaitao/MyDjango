# Generated by Django 3.1.6 on 2021-02-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two', '0004_courses_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
