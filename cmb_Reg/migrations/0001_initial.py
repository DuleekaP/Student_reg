# Generated by Django 5.0.2 on 2024-02-29 13:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvancedLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject1', models.CharField(max_length=100)),
                ('subject2', models.CharField(max_length=100)),
                ('subject3', models.CharField(max_length=100)),
                ('subject4', models.CharField(max_length=100)),
                ('result1', models.CharField(max_length=1)),
                ('result2', models.CharField(max_length=1)),
                ('result3', models.CharField(max_length=1)),
                ('result4', models.CharField(max_length=1)),
                ('resultSheet', models.FileField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BioData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('nic', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=12)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=12)),
                ('contact', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('scanned_nic', models.FileField(upload_to='')),
                ('profile_pic', models.FileField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degreeName', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=100)),
                ('gpa', models.CharField(max_length=100)),
                ('degreeClass', models.CharField(max_length=100)),
                ('degreestartYear', models.CharField(max_length=5)),
                ('graduateYear', models.CharField(max_length=5)),
                ('transcript', models.FileField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=100)),
                ('e_relationship', models.CharField(max_length=100)),
                ('e_contact', models.CharField(max_length=12)),
                ('e_address', models.CharField(max_length=100)),
                ('scanned_nic', models.FileField(upload_to='')),
                ('profile_pic', models.FileField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_designation', models.CharField(max_length=100)),
                ('c_duties', models.CharField(max_length=100)),
                ('c_contact', models.CharField(max_length=100)),
                ('c_email', models.CharField(max_length=100)),
                ('c_fax', models.CharField(max_length=100)),
                ('c_address', models.CharField(max_length=100)),
                ('p_name', models.CharField(max_length=100)),
                ('p_designation', models.CharField(max_length=100)),
                ('p_duties', models.CharField(max_length=100)),
                ('p_startDate', models.DateField()),
                ('p_endDate', models.DateField()),
                ('p_address', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        
        migrations.CreateModel(
            name='refrees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r1_name', models.CharField(max_length=100)),
                ('r1_designation', models.CharField(max_length=100)),
                ('r1_organization', models.CharField(max_length=100)),
                ('r1_contact', models.CharField(max_length=100)),
                ('r1_address', models.CharField(max_length=100)),
                ('r2_name', models.CharField(max_length=100)),
                ('r2_designation', models.CharField(max_length=100)),
                ('r2_organization', models.CharField(max_length=100)),
                ('r2_contact', models.CharField(max_length=100)),
                ('r2_address', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
