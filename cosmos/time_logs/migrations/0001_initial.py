# Generated by Django 2.1.1 on 2018-11-08 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0002_auto_20181108_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField(null=True)),
                ('description', models.TextField(null=True)),
                ('creation_type', models.PositiveSmallIntegerField(choices=[(0, 'RealTime'), (1, 'Synced'), (2, 'Added manually')], default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='time_logs', to='projects.Project')),
            ],
        ),
    ]
