# Generated by Django 3.1.6 on 2021-02-14 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('two', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='two.animals')),
            ],
        ),
    ]