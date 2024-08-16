# Generated by Django 5.1 on 2024-08-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expensive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('سیگار', 'سیگار'), ('چای', 'چای'), ('گیم نت', 'گیم نت'), ('خوراکی', 'خوراکی'), ('پوشاک', 'پوشاک'), ('غذا', 'غذا')], max_length=50)),
                ('amount', models.BigIntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
