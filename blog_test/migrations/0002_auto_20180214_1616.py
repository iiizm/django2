# Generated by Django 2.0.2 on 2018-02-14 07:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crawling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=10)),
                ('article_count', models.IntegerField(default=5)),
                ('naver_result', models.TextField(null=True)),
                ('daum_result', models.TextField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
