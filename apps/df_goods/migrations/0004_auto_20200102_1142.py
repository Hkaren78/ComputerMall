# Generated by Django 2.0.12 on 2020-01-02 11:42

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0003_auto_20190427_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(max_length=2000, verbose_name='详情'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gjianjie',
            field=models.CharField(max_length=2000, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(blank=True, null=True, upload_to='df_goods/image/%Y/%m', verbose_name='商品图片'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gprice',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.DecimalField(decimal_places=2, default='5000', max_digits=10, verbose_name='i7+512GB'),
        ),
    ]
