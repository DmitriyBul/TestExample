# Generated by Django 3.0.8 on 2020-08-12 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a title of list', max_length=200, verbose_name='Title')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')),
                ('company', models.CharField(max_length=200, verbose_name='Company')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Organization', verbose_name='Organization')),
            ],
            options={
                'verbose_name': 'ToDo list',
                'verbose_name_plural': 'ToDo lists',
                'ordering': ['published'],
            },
        ),
        migrations.DeleteModel(
            name='Todolst',
        ),
    ]
