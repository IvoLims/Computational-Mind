# Generated by Django 3.2.13 on 2022-06-28 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_quiz_question_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='backend.question'),
        ),
        migrations.AlterField(
            model_name='option',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='backend.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='backend.quiz'),
        ),
    ]