# Generated by Django 4.2.5 on 2023-09-17 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_alter_servico_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preco',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='precos', to='appointments.servico'),
        ),
    ]