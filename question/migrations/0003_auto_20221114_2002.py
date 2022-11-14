# Generated by Django 3.2.9 on 2022-11-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20221111_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_registered',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_by',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='problem_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='submission_id',
            field=models.IntegerField(null=True),
        ),
    ]