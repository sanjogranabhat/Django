# Generated by Django 5.0.3 on 2024-04-04 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_exam_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
