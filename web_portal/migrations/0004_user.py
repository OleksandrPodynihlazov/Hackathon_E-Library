# Generated by Django 5.1.1 on 2024-10-05 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_portal', '0003_alter_manual_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('last_manuals', models.ManyToManyField(to='web_portal.manual')),
            ],
        ),
    ]
