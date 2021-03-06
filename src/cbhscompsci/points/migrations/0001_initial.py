# Generated by Django 2.2.3 on 2019-08-04 05:26

from django.db import migrations, models
import django.db.models.deletion
import points.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingKey', models.CharField(default=points.models.hashKey, max_length=64)),
                ('name', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('points', models.IntegerField(default=0)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('studentNo', models.TextField()),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PointsEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('points', models.IntegerField()),
                ('reason', models.TextField()),
                ('meeting', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='points.MeetingKey')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='points.Student')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='points.MeetingKey')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='points.Student')),
            ],
        ),
    ]
