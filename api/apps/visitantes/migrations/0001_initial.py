# Generated by Django 2.2.6 on 2019-10-17 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atracoes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitorName', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('visitorPhone', models.CharField(max_length=30, verbose_name='Telefone')),
                ('visitorEmail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Seu Email')),
                ('visitorType', models.CharField(choices=[('ALUNO', 'Aluno'), ('PROFESSOR', 'Professor'), ('CONVIDADO', 'Convidado')], max_length=10, verbose_name='Tipo de Visitante')),
                ('ad', models.CharField(choices=[('WEBSITE', 'Website'), ('AMIGO', 'Amigo'), ('SOCIAL', 'Redes Sociais')], max_length=10, verbose_name='Como ouviu falar do evento')),
                ('feedback', models.TextField(verbose_name='Comentários e ou perguntas')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atracoes.Attraction')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Logado')),
            ],
        ),
    ]