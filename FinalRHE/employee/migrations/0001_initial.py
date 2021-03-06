# Generated by Django 3.1 on 2020-08-24 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='--', max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('father_first_name', models.CharField(max_length=100)),
                ('father_middle_name', models.CharField(max_length=100)),
                ('father_last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('resignation_date', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number1', models.CharField(default='123', max_length=11)),
                ('phone_number2', models.CharField(default='123', max_length=11)),
                ('address_lane1', models.CharField(max_length=100)),
                ('address_lane2', models.CharField(max_length=100)),
                ('address_lane3', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pic')),
                ('bank_name', models.CharField(max_length=100)),
                ('bank_branch', models.CharField(max_length=100)),
                ('pan_number', models.CharField(default='123', max_length=50)),
                ('account_number', models.CharField(default='123', max_length=50)),
                ('ifsc_code', models.CharField(max_length=50)),
                ('micr_code', models.CharField(max_length=50)),
                ('adharcard_number', models.CharField(default='123', max_length=50)),
                ('document1', models.ImageField(blank=True, null=True, upload_to='documents')),
                ('document2', models.ImageField(blank=True, null=True, upload_to='documents')),
                ('document3', models.ImageField(blank=True, null=True, upload_to='documents')),
                ('execution', models.IntegerField()),
                ('bd', models.IntegerField()),
                ('agreement_document', models.ImageField(blank=True, null=True, upload_to='agreement')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
