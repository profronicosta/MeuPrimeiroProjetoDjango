# Generated by Django 4.0.5 on 2022-06-29 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rh.depto'),
        ),
    ]
