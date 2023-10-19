# Generated by Django 3.2.17 on 2023-10-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0002_auto_20231017_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('describtion', models.TextField()),
                ('authname', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
