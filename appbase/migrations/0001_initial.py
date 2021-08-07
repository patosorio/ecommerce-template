# Generated by Django 3.2.6 on 2021-08-07 04:36

from django.db import migrations, models
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', isbn_field.fields.ISBNField(max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=1000)),
                ('genre', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
    ]
