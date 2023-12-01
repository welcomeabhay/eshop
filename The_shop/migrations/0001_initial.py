# Generated by Django 4.2.4 on 2023-08-10 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_name', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='pictures')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('price', models.IntegerField()),
                ('discount_p', models.FloatField(blank=True, null=True)),
                ('stock', models.IntegerField()),
                ('date_upload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=250, unique=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('img', models.ImageField(default='DEFAULT VALUE', upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Userlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('pic', models.ImageField(upload_to='Userimg')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=30)),
                ('img', models.ImageField(default='DEFAULT VALUE', upload_to='uploads')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='The_shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='The_shop.cart')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='The_shop.all_products')),
            ],
        ),
        migrations.AddField(
            model_name='all_products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='The_shop.category'),
        ),
        migrations.AddField(
            model_name='all_products',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='The_shop.sub_category'),
        ),
    ]