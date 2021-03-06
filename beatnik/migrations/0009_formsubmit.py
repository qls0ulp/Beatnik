# Generated by Django 2.1.4 on 2019-01-11 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatnik', '0008_auto_20180112_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_string', models.TextField(verbose_name='Query string')),
                ('query', models.TextField(verbose_name="The 'q' parameter in the query")),
                ('user_agent', models.TextField(null=True, verbose_name="Client's user agent")),
                ('ip_address', models.CharField(max_length=45, null=True, verbose_name="Client's IP address")),
                ('referer', models.URLField(null=True, verbose_name='HTTP referer')),
            ],
        ),
    ]
