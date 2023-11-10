# Generated by Django 4.1.5 on 2023-11-10 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0007_managementprofil_city_managementprofil_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='managementprofil',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='managementprofil',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='bithday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, choices=[('pointe_noire', 'Pointe Noire'), ('brazzaville', 'Brazzaville')], max_length=17),
        ),
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=120, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='firstname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='lastname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='student_pics'),
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(blank=True, choices=[('masculin', 'Masculin'), ('feminin', 'Féminin')], max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='tel',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='teacher',
            name='bithday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='city',
            field=models.CharField(blank=True, choices=[('pointe_noire', 'Pointe Noire'), ('brazzaville', 'Brazzaville')], max_length=17),
        ),
        migrations.AddField(
            model_name='teacher',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.CharField(blank=True, max_length=120, unique=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='end_of_contrat',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='firstname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_diploma',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='lastname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='teacher',
            name='nationality',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_pics'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='sex',
            field=models.CharField(blank=True, choices=[('masculin', 'Masculin'), ('feminin', 'Féminin')], max_length=10),
        ),
        migrations.AddField(
            model_name='teacher',
            name='start_of_contrat',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='status',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='tel',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='type_of_counter',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='user_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='user_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
