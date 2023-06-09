# Generated by Django 4.2 on 2023-05-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_remove_student_is_male_alter_student_gpa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=90)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=None)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='usn_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
