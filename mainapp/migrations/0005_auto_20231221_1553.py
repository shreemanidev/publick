# Generated by Django 3.2.23 on 2023-12-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_join_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='aadhar_upload',
            field=models.FileField(blank=True, default='', null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='join',
            name='certificate_upload',
            field=models.FileField(blank=True, default='', null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='join',
            name='contact',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='join',
            name='pan_card_upload',
            field=models.FileField(blank=True, default='', null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='join',
            name='photo_upload',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
    ]