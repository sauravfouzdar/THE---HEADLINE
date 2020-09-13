# Generated by Django 3.0.5 on 2020-05-06 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('title_of_news', models.TextField()),
                ('body_of_news', models.TextField()),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('timestamp', models.DateTimeField()),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
