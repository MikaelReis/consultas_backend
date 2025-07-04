# Generated by Django 5.2.3 on 2025-06-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profissionais', '0002_profissional_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profissional',
            old_name='especialidade',
            new_name='contato',
        ),
        migrations.RenameField(
            model_name='profissional',
            old_name='nome',
            new_name='nome_social',
        ),
        migrations.RemoveField(
            model_name='profissional',
            name='email',
        ),
        migrations.AddField(
            model_name='profissional',
            name='endereco',
            field=models.CharField(default='Sem endereco informado', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profissional',
            name='profissao',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
