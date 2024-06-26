# Generated by Django 4.1.5 on 2023-11-08 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0007_managementprofil_city_managementprofil_sex'),
        ('school_management', '0011_remove_schedule_career_remove_schedule_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCareer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_management.ademicyear')),
                ('career', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_management.career')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_management.semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_account.student')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hours', models.CharField(choices=[('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h')], max_length=15)),
                ('end_hours', models.CharField(choices=[('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h'), ('06h-07h', '06h-07h')], max_length=15)),
                ('day', models.CharField(choices=[('lundi', 'Lundi'), ('mardi', 'Mardi'), ('mercredi', 'Mercredi'), ('jeudi', 'Jeudi'), ('vendredi', 'Vendredi'), ('samedi', 'Samedi'), ('dimanche', 'Dimanche')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.career')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.subject')),
            ],
        ),
        migrations.CreateModel(
            name='SanctionAppreciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('sanction_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_management.career')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_account.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.subject')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.sanctionappreciationtype')),
            ],
        ),
    ]
