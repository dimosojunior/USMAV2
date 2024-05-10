# Generated by Django 4.1.3 on 2024-04-20 06:35

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('USMAApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=1000)),
                ('CreatedBy', models.CharField(blank=True, default='Dimoso Junior', max_length=100, null=True)),
                ('Description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('WorkImage', models.ImageField(blank=True, null=True, upload_to='media/PeopleWorksImage/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('Year', models.CharField(blank=True, default='2024', max_length=100, null=True)),
                ('Email', models.CharField(blank=True, default='juniordimoso@gmail.com', max_length=500, null=True)),
                ('Instagram', models.CharField(blank=True, default='www.instagram.com', max_length=1000, null=True)),
                ('Whatsapp', models.CharField(blank=True, default='www.whatsapp.com', max_length=1000, null=True)),
                ('Phone', models.CharField(blank=True, default='+255', max_length=13, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/PeopleWorksPDF/')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'PeopleWorks',
            },
        ),
        migrations.CreateModel(
            name='PeopleWorksCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=1000)),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/PeopleWorksImages/')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'PeopleWorksCategory',
            },
        ),
        migrations.RemoveField(
            model_name='mustuniversitycourses',
            name='university',
        ),
        migrations.RemoveField(
            model_name='udomuniversitycourses',
            name='university',
        ),
        migrations.RemoveField(
            model_name='udsmuniversitycourses',
            name='university',
        ),
        migrations.DeleteModel(
            name='DitUniversityCourses',
        ),
        migrations.DeleteModel(
            name='MustUniversityCourses',
        ),
        migrations.DeleteModel(
            name='UdomUniversityCourses',
        ),
        migrations.DeleteModel(
            name='UdsmUniversityCourses',
        ),
        migrations.AddField(
            model_name='peopleworks',
            name='Category',
            field=models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.peopleworkscategory'),
        ),
    ]
