# Generated by Django 4.0.5 on 2022-06-29 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rh', '0003_remove_funcionario_data_nascimento_funcionario_sexo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='sexo',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Depto',
        ),
    ]
