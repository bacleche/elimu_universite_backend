# Generated by Django 4.1.5 on 2023-11-08 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0013_rename_ademicyear_academicyear_and_more'),
        ('user_account', '0007_managementprofil_city_managementprofil_sex'),
        ('educational_content', '0002_bookcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='eBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('photo_cover', models.ImageField(upload_to='images_ebook')),
                ('attachement', models.FileField(upload_to='ebook_folder')),
                ('is_private', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_account.teacher')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.career')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.sector')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('code_isbn', models.CharField(max_length=120)),
                ('location', models.CharField(blank=True, max_length=120)),
                ('attachement', models.FileField(blank=True, upload_to='public_folder')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_management.sector')),
            ],
        ),
    ]
