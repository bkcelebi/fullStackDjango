# Generated by Django 3.1.3 on 2022-03-19 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20220319_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='lesson',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='choice',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=10),
        ),
    ]
