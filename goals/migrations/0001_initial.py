# Generated by Django 2.0.6 on 2018-12-17 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='goalItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_item', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(verbose_name='date published')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='goalList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_title', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='goalitem',
            name='goal_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.goalList'),
        ),
    ]
