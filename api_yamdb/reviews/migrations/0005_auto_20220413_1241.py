# Generated by Django 2.2.16 on 2022-04-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_category_genre_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='title',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='titles', to='reviews.Genre'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=None, max_length=256, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(default=None, max_length=100, verbose_name='название'),
        ),
    ]
